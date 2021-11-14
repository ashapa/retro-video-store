from app import db

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True, nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True, nullable=False)
    due_date = db.Column(db.DateTime)
    checked_in = db.Column(db.Boolean, default=False)
    
    
    #rental checked out   
    # def to_json(self, customer, video):
    #     return{
    #         "customer_id": self.customer_id,
    #         "video_id": self.video_id,
    #         "due_date": self.due_date, 
    #         "videos_checked_out_count": customer.videos_checked_out_count,
    #         "available_inventory": video.available_inventory
    #     }