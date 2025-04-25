from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Aircraft(Base):
    __tablename__ = 'aircraft'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), unique=True)
    capacity = Column(Integer)
    
class Flight(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    flight_number = Column(String(10), unique=True)
    departure = Column(DateTime)
    arrival = Column(DateTime)
    origin = Column(String(50))
    destination = Column(String(50))
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'))
    aircraft = relationship("Aircraft")
    bookings = relationship("Booking", back_populates="flight")

class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    passport = Column(String(20), unique=True)
    bookings = relationship("Booking", back_populates="passenger")

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.id'))
    passenger_id = Column(Integer, ForeignKey('passengers.id'))
    seat_number = Column(String(5))
    booking_date = Column(DateTime, default=datetime.now())
    flight = relationship("Flight", back_populates="bookings")
    passenger = relationship("Passenger", back_populates="bookings")

engine = create_engine('sqlite:///airline.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)