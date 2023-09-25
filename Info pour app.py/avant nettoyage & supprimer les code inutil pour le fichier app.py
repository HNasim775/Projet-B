from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from models import db, Order
from prestashop import fetch_product, fetch_product_qty

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db') 
SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object('config')

# order = SQLAlchemy(app)
# db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()
cache = Cache(app)

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
#@limiter.limit("5 per minute") # Adaptez selon vos besoins
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    product_data = fetch_product(product_id)
    if "error" in product_data:
        return jsonify({"error": "Failed to fetch product info from PrestaShop"}), 400
    
    # available_quantity = product_data['stock_availables']['1']['quantity']
    # available_quantity = product_data
    product_qty = fetch_product_qty(product_id)
    if "error" in product_qty:
        return jsonify({"error": "Failed to fetch product quantity from PrestaShop"}), 400
    
    # available_quantity = product_qty.get('stock_availables', {}).get('1', {}).get('quantity', 0)
    # available_quantity = int(product_qty.get('stock_availables', {}).get('quantity', 0))
    available_quantity = int(product_qty.get('prestashop', {}).get('stock_available', {}).get('quantity', 0))
    
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400

    # order.session.add(Order(product_id=product_id, quantity=quantity))
    # order.session.commit()
    # db.session.add(db(product_id=product_id, quantity=quantity))
    # db.session.commit()
    order_instance = Order(product_id=product_id, quantity=quantity)
    db.session.add(order_instance)
    db.session.commit()

    return jsonify({"message": "Added to cart successfully", "order_id": order_instance.id}), 200

@app.route('/', methods=['GET'])
def get_root():
    return "Welcome to the Order Management Microservice."


#....Configuration Flask-CORS
#CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})
app.run()
