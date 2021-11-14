from app import db
from flask import Blueprint
from app.models.customer import Customer
from app.models.video import Video
from app.models.rental import Rental
from flask import Blueprint, jsonify, request, make_response
from datetime import datetime, timedelta


customers_bp = Blueprint("customers", __name__, url_prefix="/customers")
videos_bp = Blueprint("videos", __name__, url_prefix="/videos")
rentals_bp = Blueprint("rentals", __name__, url_prefix="/rentals")


# --------------------------------
# ----------- CUSTOMERS ----------
# --------------------------------

# GET ALL CUSTOMERS
@customers_bp.route("", methods=["GET"])
def get_customers():
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

# CREATE CUSTOMER
@customers_bp.route("", methods=["POST"])
def create_customer():
    request_body = request.get_json()
    if "name" not in request_body:
        return jsonify({"details": "Request body must include name."}), 400
    elif "postal_code" not in request_body:
        return jsonify({"details": "Request body must include postal_code."}), 400
    elif "phone" not in request_body:
        return jsonify({"details": "Request body must include phone."}), 400
    
    new_customer = Customer(name = request_body["name"], 
                            postal_code = request_body["postal_code"], 
                            phone = request_body["phone"])
    
    db.session.add(new_customer)
    db.session.commit()
    
    new_customer_response = {
        "id": new_customer.id,
        "name": new_customer.name,
        "registered_at": datetime.now(),
        "postal_code": new_customer.postal_code,
        "phone": new_customer.phone
        }
    return jsonify(new_customer_response), 201


# GET CUSTOMER BY ID
@customers_bp.route("/<id>", methods=["GET"])
def get_customer(id):
    if id.isnumeric() != True:
        return {"message": "Customer id provided is not a number."}, 400
    customer = Customer.query.get(id)
    if customer is None:
        return {"message": f"Customer {id} was not found"}, 404
    else:
        # jsonify(customer.to_json()), 200
        return {
            "id": customer.id,
            "name": customer.name,
            "registered_at": customer.registered_at,"postal_code": customer.postal_code,
            "phone": customer.phone
        }, 200


# UPDATE CUSTOMER BY ID
@customers_bp.route("/<id>", methods=["PUT"])
def update_customer(id):
    customer = Customer.query.get(id)
    if customer is None:
        return {"message": f"Customer {id} was not found"}, 404
    if request.method == "PUT":
        request_body = request.get_json()
        if "name" not in request_body:
            return {"details": "Request body must include name."}, 400
        elif "postal_code" not in request_body:
            return {"details": "Request body must include postal_code."}, 400
        elif "phone" not in request_body:
            return {"details": "Request body must include phone."}, 400
    
    customer.name=request_body["name"] 
    customer.postal_code=request_body["postal_code"] 
    customer.phone=request_body["phone"] 
    db.session.commit()
    # return jsonify(customer.to_json()), 200
    return {
        "id": customer.id,
        "name": customer.name,
        "registered_at": datetime.now(),
        "postal_code": customer.postal_code,
        "phone": customer.phone}, 200


# DELETE CUSTOMER BY ID
@customers_bp.route("/<id>", methods=["DELETE"])
def delete_customer(id):
    customer = Customer.query.get(id)
    if customer is None:
        return jsonify({"message": (f"Customer {id} was not found")}), 404
    else:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"id": customer.id}), 200


# --------------------------------
# ----------- VIDEOS ----------
# --------------------------------


# GET ALL VIDEOS
@videos_bp.route("", methods=["GET"])
def get_videos():
    videos = Video.query.all()
    videos_response = []
    for video in videos:
        videos_response.append({
            "id": video.id,
            "title": video.title,
            "release_date": datetime.now(), 
            "total_inventory": video.total_inventory})
    return jsonify(videos_response), 200


# CREATE VIDEO
@videos_bp.route("", methods=["POST"])
def create_video():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body:
            return {"details": "Request body must include title."}, 400
        elif "release_date" not in request_body:
            return {"details": "Request body must include release_date."}, 400
        elif "total_inventory" not in request_body:
            return {"details": "Request body must include total_inventory."}, 400
        new_video = Video(title=request_body["title"],
                            release_date=request_body["release_date"],
                            total_inventory=request_body["total_inventory"])
        db.session.add(new_video)
        db.session.commit()
        new_video_response = {
                "id": new_video.id,
                "title": new_video.title,
                "release_date": datetime.now(), 
                "total_inventory": new_video.total_inventory
            }
        return jsonify(new_video_response), 201


# GET VIDEO BY ID
@videos_bp.route("/<id>", methods=["GET"])
def get_video(id):
    if id.isnumeric() != True:
        return {"message": "Video id provided is not a number."}, 400
    video = Video.query.get(id)
    if video is None:
        return {"message": f"Video {id} was not found"}, 404
    if request.method == "GET":  
            return {
                "id": video.id,
                "title": video.title,
                "release_date": datetime.now(), 
                "total_inventory": video.total_inventory}


# UPDATE VIDEO BY ID
@videos_bp.route("/<id>", methods=["PUT"])
def update_video(id):
    video = Video.query.get(id)
    if video is None:
        return {"message": f"Video {id} was not found"}, 404
    if request.method == "PUT":
        request_body = request.get_json()
        if "title" not in request_body:
            return {"details": "Request body must include title."}, 400
        elif "release_date" not in request_body:
            return {"details": "Request body must include release_date."}, 400
        elif "total_inventory" not in request_body:
            return {"details": "Request body must include total_inventory."}, 400
        video.title = request_body["title"]
        video.request_body = request_body["release_date"] 
        video.total_inventory = request_body["total_inventory"]
        db.session.commit()
        return {
            "id": video.id,
            "title": video.title,
            "release_date": datetime.now(), 
            "total_inventory": video.total_inventory}, 200


# DELETE VIDEO BY ID
@videos_bp.route("/<id>", methods=["DELETE"])
def delete_video(id):
    video = Video.query.get(id)
    if video is None:
        return {"message": f"Video {id} was not found"}, 404
    db.session.delete(video)
    db.session.commit()
    return {"id": video.id}, 200


# --------------------------------
# ----------- RENTALS ----------
# --------------------------------


# POST /rentals/check-out 
@rentals_bp.route("/check-out", methods=["POST"])
def checkout_video():
    
    try:
        request_body = request.get_json()
        # customer_id = request_body["customer_id"]
        # video_id = request_body["video_id"]
        customer = Customer.query.get(request_body["customer_id"])
        video = Video.query.get(request_body["video_id"])

        if customer is None or video is None:
            return make_response("", 404)
        
        if "customer_id" not in request_body or "video_id" not in request_body:
            return make_response("", 400)
        
        #check num of videos checked out
        videos_checked_out_nums = Rental.query.filter_by(video_id=request_body["video_id"], checked_in = False).count()
        available_video_inventory = video.total_inventory - videos_checked_out_nums
        if available_video_inventory == 0:
            return jsonify({"message": "Could not perform checkout"}), 400
    
    except KeyError:
        return jsonify(None), 400
        
    new_rental = Rental(
        customer_id = request_body["customer_id"], 
        video_id = request_body["video_id"], 
        due_date = datetime.now() + timedelta(days=7), 
        checked_in = False)
    
    videos_checked_out_nums += 1
    available_video_inventory -= 1
    
    db.session.add(new_rental)
    db.session.commit()
    
    return jsonify({
        "customer_id": new_rental.customer_id,
        "video_id": new_rental.video_id,
        "due_date": new_rental.due_date,
        "videos_checked_out_count": videos_checked_out_nums, 
        "available_inventory": available_video_inventory}), 200



# POST /rentals/check-in 
@rentals_bp.route("/check-in", methods=["POST"])
def checkin_video():
    request_body = request.get_json() 
    
    if "customer_id" not in request_body or "video_id" not in request_body:
        return jsonify({"message": "must provide video and customer id"}), 400
    
    customer = Customer.query.get(request_body["customer_id"])
    video = Video.query.get(request_body["video_id"])

    if customer is None:
        return make_response({"message": f"Customer {request_body['customer_id']} was not found"}, 404)     
    if video is None:
        return make_response({"message": f"Video {request_body['video_id']} was not found"}, 404)
  
    if video not in customer.videos: 
        return make_response({"message": f"No outstanding rentals for customer {request_body['customer_id']} and video {request_body['video_id']}"}), 400
    
    rented_video = Rental.query.filter_by(video_id==request_body["video_id"]).first()

    videos_checked_out_nums = Rental.query.filter_by(video_id=request_body["video_id"], checked_in = False).count()
    available_video_inventory = video.total_inventory - videos_checked_out_nums
    
    videos_checked_out_nums -= 1
    available_video_inventory += 1
 
    db.session.commit()

    return jsonify({
        "customer_id": customer.customer_id,
        "video_id": video.video_id,
        "videos_checked_out_count": videos_checked_out_nums,
        "available_inventory": available_video_inventory}), 200


