from app import db
"""
A Customer can have many Videos through a secondary table (i.e. Rentals), and a Video can be checked out/in by many Customers through the same Rentals table.
"""
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True)
    due_date = db.Column(db.DateTime)
    videos_checked_out_count = db.Column(db.Integer)
    available_inventory = db.Column(db.Integer)

    # customer = db.relationship("Customer", back_populates="videos")
    # video = db.relationship("Video", back_populates="customers")