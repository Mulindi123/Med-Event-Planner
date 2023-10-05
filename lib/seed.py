from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from models import Event, Guest, Venue
from  faker import Faker
import random
from datetime import datetime

fake = Faker()
if __name__ == "__main__":
    engine = create_engine("sqlite:///database.db")
    Session = sessionmaker(bind=engine)
    session =Session()


    session.query(Guest).delete()
    session.query(Event).delete()
    session.query(Venue).delete()

    event_names = [
    "Cosmic Carnival",
    "Enchanted Gala",
    "Midnight Masquerade",
    "Serendipity Soiree",
    "Electric Euphoria",
    "Mystic Moonlight Mixer",
    "Whimsical Wonderland",
    "Oceanic Odyssey",
    "Luminous Labyrinth",
    "Secret Garden Affair"
]
    events = []
    for i in range(10):
        event = Event(
            event_name = random.choice(event_names),
            date = datetime.strptime(fake.date(), '%Y-%m-%d'),
            description= fake.sentence()
        )
        session.add(event)
        session.commit()
        events.append(event)
    
    guests = []
    for i in range(10):
        guest=Guest(
            guest_name = fake.name()
        )
        session.add(guest)
        session.commit()
        guests.append(guest)


    venue_names = [
    "Sarova Stanley",
    "Nairobi National Park",
    "Karen Blixen Coffee Garden",
    "Bomas of Kenya",
    "Giraffe Manor",
    "KICC (Kenyatta International Convention Centre)",
    "Nairobi Safari Walk",
    "Kazuri Beads Women's Cooperative",
    "The Hub Karen",
    "Nairobi Railway Museum"
]
    venues = []
    for i in range(10):
        venue =Venue(
           venue_name = random.choice(venue_names),
           address = fake.address(),
           event_id = random.randint(1, 10),        
        )
        session.add(venue)
        session.commit()
        venues.append(venue)

    for event in events:
        num_attendees = random.randint(1, 5)
        attendees = random.sample(guests, num_attendees)
        event.guests.extend(attendees)

    for venue in venues:
        num_guests = random.randint(1, 5)
        guests_to_assign = random.sample(guests, num_guests)
        venue.guests.extend(guests_to_assign)
    session.commit()

    session.close()
