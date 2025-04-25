from models import Session, Flight, Passenger, Booking, Aircraft
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

class DataAccessLayer:
    def __init__(self):
        self.session = Session()
    
    def create_flight(self, flight):
        try:
            self.session.add(flight)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False

    def get_flights(self, origin=None, destination=None):
        query = self.session.query(Flight)
        if origin:
            query = query.filter(Flight.origin == origin)
        if destination:
            query = query.filter(Flight.destination == destination)
        return query.all()
    
    def create_passenger(self, passenger):
        try:
            self.session.add(passenger)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
    
    def create_booking(self, booking):
        try:
            self.session.add(booking)
            self.session.commit()
            return True
        except IntegrityError:
            self.session.rollback()
            return False
    
    def get_flight_occupancy(self, flight_id):
        result = self.session.query(
            Flight.flight_number,
            func.count(Booking.id).label('booked_seats'),
            Aircraft.capacity
        ).outerjoin(Booking)\
         .join(Aircraft)\
         .filter(Flight.id == flight_id)\
         .group_by(Flight.id).first()
        
        return result