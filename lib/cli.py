
import click
from methods import create_event, create_guest, create_venue


@click.group()
def cli():
    """Med's Evnt Planner."""


#  add a new event
@cli.command()
@click.option("--event-name", prompt="Event name", help="Name of the event")
@click.option("--date", prompt="Date of the event", help="Date of the event (YYYY-MM-DD)")
@click.option("--description", prompt="Event description", help="Description of the event")
def add_event(event_name, date, description):
    """Add a new event."""
    event = create_event(event_name, date, description)
    click.echo(f"Event added successfully. Event ID: {event.id}")

# add a new guest
@cli.command()
@click.option("--guest-name", prompt="Guest name", help="Name of the guest")
def add_guest(guest_name):
    """Invite a guest to an event"""
    guest = create_guest(guest_name)
    click.echo(f"Guest added successfully. Guest ID: {guest.id}")

# add a new venue
@cli.command()
@click.option("--venue-name", prompt="Venue name", help="Name of the venue")
@click.option("--address", prompt="Venue address", help="Address of the venue")
def addvenue(venue_name, address):
    """Add a new venue."""
    venue = create_venue(venue_name, address)
    click.echo(f"Venue added successfully. Venue ID: {venue.id}")


if __name__ == "__main__":
    cli()
