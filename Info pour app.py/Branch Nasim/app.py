from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Order
from prestashop import fetch_product_qty
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db') 
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
with app.app_context():
    db.create_all()

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found!"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error!"}), 500

@app.route('/')
def hello():
    return "<h1>The Micro-Service A for Order Management is providing...</h1>"

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    product_qty = fetch_product_qty(product_id)
    if "error" in product_qty:
        return jsonify({"error": "Failed to fetch product quantity from PrestaShop"}), 400

    available_quantity = int(product_qty.get('prestashop', {}).get('stock_available', {}).get('quantity', 0))
    
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400

    order_instance = Order(product_id=product_id, quantity=quantity)
    db.session.add(order_instance)
    db.session.commit()

    return jsonify({"message": "Added to cart successfully", "order_id": order_instance.id}), 200

if __name__ == '__main__':
    app.run()

