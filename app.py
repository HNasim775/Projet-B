# Importation des modules nécessaires
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Order  # Importe des objets de votre modèle de données
from prestashop import fetch_product_qty  # Importe une fonction pour récupérer la quantité de produits
import os

# Configuration de la base de données SQLite
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Création de l'application Flask
app = Flask(__name__)
app.config.from_object('my_config')

# Initialisation de la base de données avec l'application Flask
db.init_app(app)
with app.app_context():
    db.create_all()

# Gestion des erreurs 404 (ressource non trouvée) et 500 (erreur interne du serveur)
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found!"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error!"}), 500

# Définition d'une route pour la page d'accueil
@app.route('/')
def hello():
    return "<h1>The Micro-Service A for Order Management is providing...</h1>"

# Définition d'une route pour ajouter un produit au panier
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Récupération des données du produit à ajouter depuis la requête JSON
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    # Récupération de la quantité disponible du produit depuis PrestaShop
    product_qty = fetch_product_qty(product_id)
    
    # Gestion des erreurs
    if "error" in product_qty:
        return jsonify({"error": "Failed to fetch product quantity from PrestaShop"}), 400

    available_quantity = int(product_qty.get('prestashop', {}).get('stock_available', {}).get('quantity', 0))
    
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400

    # Création d'une instance de commande et ajout à la base de données
    order_instance = Order(product_id=product_id, quantity=quantity)
    db.session.add(order_instance)
    db.session.commit()

    return jsonify({"message": "Added to cart successfully", "order_id": order_instance.id}), 200

# Exécution de l'application Flask si le script est exécuté directement
if __name__ == '__main__':
    app.run()
