#!/usr/bin/env python3

import click
from datetime import date
from methods import create_event, create_guest, create_venue, \
    get_event_by_id, get_guest_by_id, get_venue_by_id, \
    list_all_events, list_all_guests, list_all_venues, \
    delete_event_by_id, delete_guest_by_id, delete_venue_by_id

def print_menu():
    """Print the interactive menu options."""
    click.echo("Welcome to Med's Event Planner")
    click.echo("Menu:")
    click.echo("1. Search for an entity by ID")
    click.echo("2. Create a new entity")
    click.echo("3. List all entities of a given type")
    click.echo("4. Delete an entity by ID")
    click.echo("5. Exit")

@click.group()
def cli():
    """Welcome to Med's Event Planner"""

@cli.command()
def menu():
    """Display the interactive menu."""
    while True:
        print_menu()
        choice = click.prompt("Enter your choice (1-5)", type=int)
        if choice == 1:
            search()
        elif choice == 2:
            create()
        elif choice == 3:
            list_entities()
        elif choice == 4:
            delete()
        elif choice == 5:
            click.echo("Exiting Med's Event Planner. Goodbye!")
            break
        else:
            click.echo("Invalid choice. Please enter a number between 1 and 5.")

def search():
    """Search for an entity by ID."""
    click.echo("Search for an entity by ID:")
    entity = click.prompt("Enter entity type (event, guest, venue)", type=str)
    entity = entity.lower()
    if entity not in ['event', 'guest', 'venue']:
        click.echo("Invalid entity type. Please enter 'event', 'guest', or 'venue'.")
        return
    id = click.prompt("Enter entity ID", type=int)
    if entity == 'event':
        event = get_event_by_id(id)
        if event:
            click.echo(f"Event ID: {event.id}, Event Name: {event.event_name}")
        else:
            click.echo(f"Event with ID {id} not found.")
    elif entity == 'guest':
        guest = get_guest_by_id(id)
        if guest:
            click.echo(f"Guest ID: {guest.id}, Guest Name: {guest.guest_name}")
        else:
            click.echo(f"Guest with ID {id} not found.")
    elif entity == 'venue':
        venue = get_venue_by_id(id)
        if venue:
            click.echo(f"Venue ID: {venue.id}, Venue Name: {venue.venue_name}")
        else:
            click.echo(f"Venue with ID {id} not found.")

def create():
    """Create a new entity."""
    click.echo("Create a new entity:")
    entity = click.prompt("Enter entity type (event, guest, venue)", type=str)
    entity = entity.lower()
    if entity not in ['event', 'guest', 'venue']:
        click.echo("Invalid entity type. Please enter 'event', 'guest', or 'venue'.")
        return
    name = click.prompt("Enter entity name", type=str)
    if entity == 'event':
        description = click.prompt("Enter event description: ", default='', type=str)
        event_date = click.prompt("Enter event date (YYYY-MM-DD): ", default=date.today().strftime("%Y-%m-%d"))
        event = create_event(name, description, event_date)
        click.echo(f"Event '{event.event_name}' with ID {event.id} created successfully.")
    elif entity == 'guest':
        guest = create_guest(name)
        click.echo(f"Guest '{guest.guest_name}' with ID {guest.id} created successfully.")
    elif entity == 'venue':
        address = click.prompt("Enter venue address (optional)", default='', type=str)
        venue = create_venue(name, address)
        click.echo(f"Venue '{venue.venue_name}' with ID {venue.id} created successfully.")

def list_entities():
    """List all entities of a given type."""
    click.echo("List all entities of a given type:")
    entity = click.prompt("Enter entity type (event, guest, venue)", type=str)
    entity = entity.lower()
    if entity not in ['event', 'guest', 'venue']:
        click.echo("Invalid entity type. Please enter 'event', 'guest', or 'venue'.")
        return
    if entity == 'event':
        events = list_all_events()
        if events:
            for event in events:
                click.echo(f"Event ID: {event.id}, Event Name: {event.event_name}")
        else:
            click.echo("No events available.")
    elif entity == 'guest':
        guests = list_all_guests()
        if guests:
            for guest in guests:
                click.echo(f"Guest ID: {guest.id}, Guest Name: {guest.guest_name}")
        else:
            click.echo("No guests available.")
    elif entity == 'venue':
        venues = list_all_venues()
        if venues:
            for venue in venues:
                click.echo(f"Venue ID: {venue.id}, Venue Name: {venue.venue_name}")
        else:
            click.echo("No venues available.")

def delete():
    """Delete an entity by ID."""
    click.echo("Delete an entity by ID:")
    entity = click.prompt("Enter entity type (event, guest, venue)", type=str)
    entity = entity.lower()
    if entity not in ['event', 'guest', 'venue']:
        click.echo("Invalid entity type. Please enter 'event', 'guest', or 'venue'.")
        return
    id = click.prompt("Enter entity ID", type=int)
    if entity == 'event':
        if delete_event_by_id(id):
            click.echo(f"Event with ID {id} deleted successfully.")
        else:
            click.echo(f"Event with ID {id} not found.")
    elif entity == 'guest':
        if delete_guest_by_id(id):
            click.echo(f"Guest with ID {id} deleted successfully.")
        else:
            click.echo(f"Guest with ID {id} not found.")
    elif entity == 'venue':
        if delete_venue_by_id(id):
            click.echo(f"Venue with ID {id} deleted successfully.")
        else:
            click.echo(f"Venue with ID {id} not found.")

if __name__ == '__main__':
    cli()
