
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import declarative_base, relationship, backref


Base = declarative_base()


# Defines the many to many relationship between guests and events
guest_event_association = Table(
    "event_guests",
    Base.metadata,
    Column('guest_id', Integer, ForeignKey('guests.id'), primary_key = True),
    Column('event_id', Integer, ForeignKey('events.id'), primary_key= True),
    extend_existing = True
)

# Creating the event class
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key = True)
    event_name = Column(String, nullable=False)
    date = Column(Date, nullable= False)
    description = Column(String)
    # venue_id = Column(Integer, ForeignKey('venues.id'))

 # Relationships
 #Event - Guest (many to many)-An event can have multiple guests and a guest
 #can attend many events(association table)
 #Event-Venue(An event has one venue, and a venue can host many events)->one to many
 #Event(one----relationship(venues))-----venues(many-----foreignkey(event_id))
 #Guest- Venue (a guest can be in one venue, and a venue can have many guests)->one to many
 #Guest(one----relashionship(venues))----venues(many----foreignKey(guest_id))


    #Defines relationships
    venues = relationship('Venue', backref=backref('event'))
    guests = relationship('Guest', secondary=guest_event_association, back_populates='events')

    # Method to provide a string representation of the event object
    def __repr__(self):
        return f"Event name: {self.event_name},"\
            +f"Date of Event: {self.date},"\
            +f"Event description: {self.description}"
    


class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key = True)
    guest_name = Column(String, nullable = False)
    venue_id = Column(Integer, ForeignKey('venues.id'))
 
    #Defines relationships
    events = relationship('Event', secondary=guest_event_association, back_populates='guests')
    venues = relationship('Venue', backref=backref('guest'))


    # Method to provide a string representation of the guest object
    def __repr__(self):
        return f"Name of guest: {self.guest_name}"
            

    

class Venue(Base): 
    __tablename__ = "venues"
    id = Column(Integer, primary_key = True)
    venue_name = Column(String, nullable = False)
    address = Column(String)
    event_id =Column(Integer, ForeignKey("events.id"))
    guest_id = Column(Integer, ForeignKey("guests.id"))

    #Defines relationships
    #events = relationship('Event', backref=backref('venues'))
    # guests = relationship('Guest', back_populates='venues')
    
     # Method to provide a string representation of the venue object
    def __repr__(self):
        return f"Name of Venue: {self.venue_name},"\
            +f"Physical address: {self.address}"
            
