from models import Flight, Session
from dal import DataAccessLayer
import pytest

@pytest.fixture
def dal():
    return DataAccessLayer()

def test_create_flight(dal):
    test_flight = Flight(flight_number="SL100", origin="JFK", destination="LHR")
    result = dal.create_flight(test_flight)
    assert result is True