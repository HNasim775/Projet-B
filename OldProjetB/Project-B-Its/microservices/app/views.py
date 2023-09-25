from flask import request, jsonify
from app import app, db
from app.models import Order
from prestashop import fetch_product

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_it = request.json.get('product_id')
    quantity = request.json.get('quantity')
    
    product_data = fetch_product(product_id)
    if not product_data:
        return jsonify({"error": "Failed to fetch product infor from PrestaShop"}), 500
    
    available_quantity = product_data['stock_availables']['1']['quantity']
    
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400
    
    order = order(product_id=product_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    
    return jsonify({"message": "Added to cart sucessfull", "order_it": order.id}), 2


# ... autres imports

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500    