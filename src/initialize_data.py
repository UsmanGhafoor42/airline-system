from models import Session, Aircraft

def initialize():
    session = Session()
    aircrafts = [
        Aircraft(model="Airbus A320", capacity=180),
        Aircraft(model="Boeing 737", capacity=178),
        Aircraft(model="Airbus A380", capacity=555)
    ]
    session.add_all(aircrafts)
    session.commit()
    print("Initialized aircraft data!")

if __name__ == "__main__":
    initialize()