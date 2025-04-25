import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) ) # Add this

from src.models import Flight, Aircraft, Session  # Now this will work
from src.dal import DataAccessLayer

import logging

# Set up logging configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

import pytest
from src.models import Flight, Aircraft, Session, Booking, Passenger
from src.dal import DataAccessLayer

@pytest.fixture
def dal():
    return DataAccessLayer()

def test_create_aircraft(dal):
    aircraft = Aircraft(model="Boeing 747", capacity=416)
    assert dal.create_flight(aircraft) == True
    logging.info("Aircraft created successfully")

def test_flight_occupancy(dal):
    result = dal.get_flight_occupancy(1)
    assert result is not None
    logging.info("Flight occupancy retrieved successfully")