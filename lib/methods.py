from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Event, Guest, Venue
from datetime import datetime


# Initializes the database and creates a session
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
session = Session()


#Method to create an event
def create_event(event_name, date, description):
    event = Event(event_name=event_name, date = datetime.strptime(date, "%Y-%m-%d").date(), description=description)
    session.add(event)
    session.commit()
    return event

#Method to invite guests
def create_guest(guest_name):
    guest = Guest(guest_name=guest_name)
    session.add(guest)
    session.commit()
    return guest


#method to add a venue
def create_venue(venue_name, address):
    venue = Venue(venue_name=venue_name, address=address)
    session.add(venue)
    session.commit()
    return venue

