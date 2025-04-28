# Data storage (using simple lists instead of a database)
# `trips` stores details of all trips
# `travelers` stores details of all travelers
# `trip_legs` stores details of individual trip legs
# `users` stores user accounts (coordinators, managers, and administrators)
trips = []
travelers = []
trip_legs = []
users = []

# Default admin user
# Predefined administrator account for initial access
users.append({
    "id": "admin1",  # Unique ID for the admin
    "username": "admin",  # Admin username
    "password": "admin123",  # Admin password
    "role": "administrator"  # Role of the user
})


# Helper functions
def clear_screen():
    """
    Clear the console screen.
    Uses `cls` for Windows and `clear` for other operating systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_input(prompt, allow_empty=False):
    """
    Get user input with optional validation.
    :param prompt: The message to display to the user.
    :param allow_empty: Whether empty input is allowed.
    :return: The user's input.
    """
    while True:
        value = input(prompt)
        if value or allow_empty:  # Allow empty input if specified
            return value
        print("This field cannot be empty. Please try again.")


def get_date_input(prompt):
    """
    Get a valid date input from the user.
    :param prompt: The message to display to the user.
    :return: A `datetime.date` object representing the entered date.
    """
    while True:
        date_str = input(prompt + " (DD/MM/YYYY): ")
        try:
            # Parse the date string into day, month, and year
            day, month, year = map(int, date_str.split('/'))
            return datetime.date(year, month, day)  # Return a `datetime.date` object
        except:
            print("Invalid date format. Please use DD/MM/YYYY.")


def get_int_input(prompt):
    """
    Get integer input with validation.
    :param prompt: The message to display to the user.
    :return: An integer value.
    """
    while True:
        try:
            return int(input(prompt))  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number.")


# Trip management functions
def create_trip():
    """
    Create a new trip and add it to the `trips` list.
    """
    print("\n=== Create New Trip ===")

    # Collect trip details from the user
    trip = {
        "id": str(uuid.uuid4())[:8],  # Generate a short unique ID for the trip
        "name": get_input("Trip Name: "),  # Name of the trip
        "start_date": get_date_input("Start Date"),  # Start date of the trip
        "duration": get_int_input("Duration (days): "),  # Duration of the trip in days
        "coordinator": get_input("Trip Coordinator ID: "),  # ID of the trip coordinator
        "contact": get_input("Contact Information: "),  # Contact details for the trip
        "travelers": [],  # List of traveler IDs associated with the trip
        "legs": []  # List of trip leg IDs associated with the trip
    }

    trips.append(trip)  # Add the trip to the `trips` list
    print(f"Trip '{trip['name']}' created successfully with ID: {trip['id']}")


def view_trips():
    """
    Display all trips in the system.
    """
    print("\n=== All Trips ===")

    if not trips:  # Check if there are no trips
        print("No trips found.")
        return

    # Iterate through each trip and display its details
    for trip in trips:
        print(f"ID: {trip['id']}")
        print(f"Name: {trip['name']}")
        print(f"Start Date: {trip['start_date'].strftime('%d/%m/%Y')}")  # Format the date for display
        print(f"Duration: {trip['duration']} days")
        print(f"Coordinator: {trip['coordinator']}")
        print(f"Number of Travelers: {len(trip['travelers'])}")  # Count the number of travelers
        print(f"Number of Trip Legs: {len(trip['legs'])}")  # Count the number of trip legs
        print("-" * 30)  # Separator for readability


def update_trip():
    """
    Update the details of an existing trip.
    """
    trip_id = get_input("\nEnter Trip ID to update: ")  # Get the trip ID from the user

    for trip in trips:  # Search for the trip with the given ID
        if trip['id'] == trip_id:
            print(f"Updating Trip: {trip['name']}")

            # Update each field, allowing the user to leave it unchanged
            trip['name'] = get_input(f"Trip Name [{trip['name']}]: ", True) or trip['name']

            date_str = get_input(f"Start Date [{trip['start_date'].strftime('%d/%m/%Y')}] (DD/MM/YYYY): ", True)
            if date_str:
                try:
                    day, month, year = map(int, date_str.split('/'))
                    trip['start_date'] = datetime.date(year, month, day)
                except:
                    print("Invalid date format. Start date not updated.")

            duration_str = get_input(f"Duration [{trip['duration']}] days: ", True)
            if duration_str:
                try:
                    trip['duration'] = int(duration_str)
                except:
                    print("Invalid number. Duration not updated.")

            trip['coordinator'] = get_input(f"Trip Coordinator ID [{trip['coordinator']}]: ", True) or trip['coordinator']
            trip['contact'] = get_input(f"Contact Information [{trip['contact']}]: ", True) or trip['contact']

            print(f"Trip '{trip['name']}' updated successfully")
            return

    print(f"Trip with ID {trip_id} not found.")  # If no trip matches the given ID


def delete_trip():
    """
    Delete a trip from the system.
    """
    trip_id = get_input("\nEnter Trip ID to delete: ")  # Get the trip ID from the user

    for i, trip in enumerate(trips):  # Search for the trip with the given ID
        if trip['id'] == trip_id:
            trip_name = trip['name']
            del trips[i]  # Remove the trip from the list
            print(f"Trip '{trip_name}' deleted successfully")
            return

    print(f"Trip with ID {trip_id} not found.")  # If no trip matches the given ID


# Traveler management functions
def create_traveler():
    """Create a new traveler profile"""
    print("\n=== Create New Traveler ===")

    traveler = {
        "id": str(uuid.uuid4())[:8],  # Generate a short unique ID
        "name": get_input("Full Name: "),
        "address": get_input("Address: "),
        "dob": get_date_input("Date of Birth"),
        "emergency_contact": get_input("Emergency Contact: "),
        "gov_id_type": get_input("Government ID Type: "),
        "gov_id_number": get_input("Government ID Number: ")
    }

    travelers.append(traveler)
    print(f"Traveler '{traveler['name']}' created successfully with ID: {traveler['id']}")


def view_travelers():
    """Display all travelers"""
    print("\n=== All Travelers ===")

    if not travelers:
        print("No travelers found.")
        return

    for traveler in travelers:
        print(f"ID: {traveler['id']}")
        print(f"Name: {traveler['name']}")
        print(f"Date of Birth: {traveler['dob'].strftime('%d/%m/%Y')}")
        print(f"ID Type: {traveler['gov_id_type']}")
        print(f"ID Number: {traveler['gov_id_number']}")
        print("-" * 30)


def update_traveler():
    """Update an existing traveler"""
    traveler_id = get_input("\nEnter Traveler ID to update: ")

    for traveler in travelers:
        if traveler['id'] == traveler_id:
            print(f"Updating Traveler: {traveler['name']}")

            traveler['name'] = get_input(f"Full Name [{traveler['name']}]: ", True) or traveler['name']
            traveler['address'] = get_input(f"Address [{traveler['address']}]: ", True) or traveler['address']

            date_str = get_input(f"Date of Birth [{traveler['dob'].strftime('%d/%m/%Y')}] (DD/MM/YYYY): ", True)
            if date_str:
                try:
                    day, month, year = map(int, date_str.split('/'))
                    traveler['dob'] = datetime.date(year, month, day)
                except:
                    print("Invalid date format. Date of birth not updated.")

            traveler['emergency_contact'] = get_input(f"Emergency Contact [{traveler['emergency_contact']}]: ", True) or \
                                            traveler['emergency_contact']
            traveler['gov_id_type'] = get_input(f"Government ID Type [{traveler['gov_id_type']}]: ", True) or traveler[
                'gov_id_type']
            traveler['gov_id_number'] = get_input(f"Government ID Number [{traveler['gov_id_number']}]: ", True) or \
                                        traveler['gov_id_number']

            print(f"Traveler '{traveler['name']}' updated successfully")
            return

    print(f"Traveler with ID {traveler_id} not found.")


def delete_traveler():
    """Delete a traveler"""
    traveler_id = get_input("\nEnter Traveler ID to delete: ")

    for i, traveler in enumerate(travelers):
        if traveler['id'] == traveler_id:
            traveler_name = traveler['name']
            del travelers[i]
            print(f"Traveler '{traveler_name}' deleted successfully")
            return

    print(f"Traveler with ID {traveler_id} not found.")

