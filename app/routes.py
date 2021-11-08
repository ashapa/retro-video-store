from app import db
from flask import Blueprint
from app.models.customer import Customer
from app.models.video import Video
from flask import Blueprint, jsonify, request, make_response
from datetime import datetime


customers_bp = Blueprint("customers", __name__, url_prefix="/customers")
videos_bp = Blueprint("videos", __name__, url_prefix="/videos")


@customers_bp.route("", methods=["GET"])
def get_all_customers():
    if request.method == "GET":
        customers = Customer.query.all()
        customers_response = []
    for customer in customers:
        customers_response.append({
            "id": customer.id,
            "name": customer.name,
            "registered_at": datetime.now(), 
            "postal_code": customer.postal_code, 
            "phone": customer.phone})
        
    return jsonify(customers_response), 200








# @customers_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
# def handle_single_customer(customer_id):