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
    event = Event(event_name=event_name, date = date, description=description)
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


# Query event by ID
def get_event_by_id(event_id):
    return session.query(Event).filter(Event.id == event_id).first()

# Query guest by ID
def get_guest_by_id(guest_id):
    return session.query(Guest).filter(Guest.id == guest_id).first()

# Query venue by ID
def get_venue_by_id(venue_id):
    return session.query(Venue).filter(Venue.id == venue_id).first()

# List all available events
def list_all_events():
    return session.query(Event).all()

# List all guests invited to an event by event ID
def list_guests_by_event_id(event_id):
    event = get_event_by_id(event_id)
    if event:
        return event.guests
    return []

# List all available venues
def list_all_venues():
    return session.query(Venue).all()

# List all available guests
def list_all_guests():
    return session.query(Guest).all()

# Delete event by ID
def delete_event_by_id(event_id):
    event = get_event_by_id(event_id)
    if event:
        session.delete(event)
        session.commit()
        return True
    return False

# Delete guest by ID
def delete_guest_by_id(guest_id):
    guest = get_guest_by_id(guest_id)
    if guest:
        session.delete(guest)
        session.commit()
        return True
    return False

# Delete venue by ID
def delete_venue_by_id(venue_id):
    venue = get_venue_by_id(venue_id)
    if venue:
        session.delete(venue)
        session.commit()
        return True
    return False


