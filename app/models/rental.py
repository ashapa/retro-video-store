from app import db
"""
a Customer can have many Videos through a secondary table (i.e. Rentals), and a Video can be checked out/in by many Customers through the same Rentals table.
"""
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True, nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    # videos_checked_out_count = db.Column(db.Integer)
    # available_inventory = db.Column(db.Integer)
    check_in_status: db.Column(db.Boolean, default=False)

    customer = db.relationship("Customer", backref="rentals")
    video = db.relationship("Video", backref="rentals")
    
    #rental checked out   
    # def to_json(self, customer, video):
    #     return{
    #         "customer_id": self.customer_id,
    #         "video_id": self.video_id,
    #         "due_date": self.due_date, 
    #         "videos_checked_out_count": customer.videos_checked_out_count,
    #         "available_inventory": video.available_inventory
    #     }