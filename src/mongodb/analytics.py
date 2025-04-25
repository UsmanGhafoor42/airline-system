from pymongo import MongoClient
from datetime import datetime

class Analytics:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client.airline_analytics
    
    def log_booking(self, booking_id):
        self.db.bookings.insert_one({
            'booking_id': booking_id,
            'timestamp': datetime.now(),
            'event': 'booking_created'
        })
    
    def get_booking_stats(self):
        return self.db.bookings.aggregate([{
            '$group': {
                '_id': None,
                'total_bookings': {'$sum': 1},
                'latest_booking': {'$max': '$timestamp'}
            }
        }])