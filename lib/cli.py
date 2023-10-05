
import click
from methods import create_event, create_guest, create_venue,list_guests_by_event_id
from methods import get_event_by_id,get_guest_by_id,get_venue_by_id,list_all_events
from methods import  list_all_venues,delete_event_by_id,delete_guest_by_id,delete_venue_by_id


@click.group()
def cli():
    """Welcome to Med's Event Planner."""


#  add a new event
@cli.command()
@click.option("--event_name", prompt="Event name", help="Name of the event")
@click.option("--date", prompt="Date of the event", help="Date of the event (YYYY-MM-DD)")
@click.option("--description", prompt="Event description", help="Description of the event")
def add_event(event_name, date, description):
    """Add a new event."""
    event = create_event(event_name, date, description)
    click.echo(f"Event {event.id} has been added successfully!")

# add a new guest
@cli.command()
@click.option("--guest_name", prompt="Guest name", help="Name of the guest")
def add_guest(guest_name):
    """Invite a guest to an event"""
    guest = create_guest(guest_name)
    click.echo(f"Guest {guest.id} has been added successfully!")

# add a new venue
@cli.command()
@click.option("--venue_name", prompt="Venue name", help="Name of the venue")
@click.option("--address", prompt="Venue address", help="Address of the venue")
def add_venue(venue_name, address):
    """Add a new venue."""
    venue = create_venue(venue_name, address)
    click.echo(f"Venue {venue.id} has been added succesfully")



# ...

# Create a command to query an event by ID
@cli.command()
@click.argument("event_id", type=int)
def get_event(event_id):
    """Query an event by ID."""
    event = get_event_by_id(event_id)
    if event:
        click.echo(f"Event ID: {event.id}, Event Name: {event.event_name}")
    else:
        click.echo(f"Event with ID {event_id} not found.")

# Create a command to query a guest by ID
@cli.command()
@click.argument("guest_id", type=int)
def get_guest(guest_id):
    """Query a guest by ID."""
    guest = get_guest_by_id(guest_id)
    if guest:
        click.echo(f"Guest ID: {guest.id}, Guest Name: {guest.guest_name}")
    else:
        click.echo(f"Guest with ID {guest_id} not found.")

# Create a command to query a venue by ID
@cli.command()
@click.argument("venue_id", type=int)
def get_venue(venue_id):
    """Query a venue by ID."""
    venue = get_venue_by_id(venue_id)
    if venue:
        click.echo(f"Venue ID: {venue.id}, Venue Name: {venue.venue_name}")
    else:
        click.echo(f"Venue with ID {venue_id} not found.")

# Create a command to list all events
@cli.command()
def list_events():
    """List all available events."""
    events = list_all_events()
    if events:
        for event in events:
            click.echo(f"Event ID: {event.id}, Event Name: {event.event_name}")
    else:
        click.echo("No events available.")

# Create a command to list all guests invited to an event by event ID
@cli.command()
@click.argument("event_id", type=int)
def list_guests(event_id):
    """List all guests invited to an event by event ID."""
    guests = list_guests_by_event_id(event_id)
    if guests:
        for guest in guests:
            click.echo(f"Guest ID: {guest.id}, Guest Name: {guest.guest_name}")
    else:
        click.echo(f"No guests found for event with ID {event_id}.")

# Create a command to list all venues
@cli.command()
def list_venues():
    """List all available venues."""
    venues = list_all_venues()
    if venues:
        for venue in venues:
            click.echo(f"Venue ID: {venue.id}, Venue Name: {venue.venue_name}")
    else:
        click.echo("No venues available.")

# Create a command to delete an event by ID
@cli.command()
@click.argument("event_id", type=int)
def delete_event(event_id):
    """Delete an event by ID."""
    if delete_event_by_id(event_id):
        click.echo(f"Event with ID {event_id} deleted successfully.")
    else:
        click.echo(f"Event with ID {event_id} not found.")

# Create a command to delete a guest by ID
@cli.command()
@click.argument("guest_id", type=int)
def delete_guest(guest_id):
    """Delete a guest by ID."""
    if delete_guest_by_id(guest_id):
        click.echo(f"Guest with ID {guest_id} deleted successfully.")
    else:
        click.echo(f"Guest with ID {guest_id} not found.")

# Create a command to delete a venue by ID
@cli.command()
@click.argument("venue_id", type=int)
def delete_venue(venue_id):
    """Delete a venue by ID."""
    if delete_venue_by_id(venue_id):
        click.echo(f"Venue with ID {venue_id} deleted successfully.")
    else:
        click.echo(f"Venue with ID {venue_id} not found.")



if __name__ == "__main__":
    cli()
