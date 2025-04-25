from dal import DataAccessLayer
from models import Flight, Passenger, Booking, Aircraft
from datetime import datetime

class BusinessLogic:
    def __init__(self):
        self.dal = DataAccessLayer()
    
    def schedule_flight(self, flight_data):
        if flight_data.departure >= flight_data.arrival:
            raise ValueError("Arrival must be after departure")
        
        aircraft = self.dal.session.query(Aircraft).get(flight_data.aircraft_id)
        if not aircraft:
            raise ValueError("Invalid aircraft ID")
        
        return self.dal.create_flight(flight_data)
    
    def book_flight(self, passenger_data, flight_id, seat_number):
        flight = self.dal.session.query(Flight).get(flight_id)
        if not flight:
            raise ValueError("Invalid flight ID")
        
        existing_booking = self.dal.session.query(Booking).filter_by(
            flight_id=flight_id,
            seat_number=seat_number
        ).first()
        
        if existing_booking:
            raise ValueError("Seat already occupied")
        
        passenger = Passenger(**passenger_data)
        if not self.dal.create_passenger(passenger):
            raise ValueError("Passenger already exists")
        
        booking = Booking(
            flight_id=flight_id,
            passenger_id=passenger.id,
            seat_number=seat_number
        )
        return self.dal.create_booking(booking)
    
    def get_flight_occupancy(self, flight_id):
        return self.dal.get_flight_occupancy(flight_id)