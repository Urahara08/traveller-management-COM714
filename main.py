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

# Trip leg management functions

def create_trip_leg():
    """Create a new trip leg"""
    print("\n=== Create New Trip Leg ===")

    trip_id = get_input("Trip ID: ")

    # Check if trip exists
    trip_exists = False
    for trip in trips:
        if trip['id'] == trip_id:
            trip_exists = True
            break

    if not trip_exists:
        print(f"Trip with ID {trip_id} not found.")
        return

    leg = {
        "id": str(uuid.uuid4())[:8],  # Generate a short unique ID
        "trip_id": trip_id,
        "start_location": get_input("Starting Location: "),
        "destination": get_input("Destination: "),
        "transport_provider": get_input("Transport Provider: "),
        "transport_mode": get_input("Mode of Transport: "),
        "leg_type": get_input("Leg Type (accommodation/poi/transfer): "),
        "cost": get_int_input("Cost: ")
    }

    trip_legs.append(leg)

    # Add leg reference to trip
    for trip in trips:
        if trip['id'] == trip_id:
            trip['legs'].append(leg['id'])

    print(f"Trip leg created successfully with ID: {leg['id']}")


def view_trip_legs():
    """Display all trip legs"""
    print("\n=== All Trip Legs ===")

    if not trip_legs:
        print("No trip legs found.")
        return

    for leg in trip_legs:
        print(f"ID: {leg['id']}")
        print(f"Trip ID: {leg['trip_id']}")
        print(f"Route: {leg['start_location']} to {leg['destination']}")
        print(f"Transport: {leg['transport_mode']} by {leg['transport_provider']}")
        print(f"Type: {leg['leg_type']}")
        print(f"Cost: ${leg['cost']}")
        print("-" * 30)


def update_trip_leg():
    """Update an existing trip leg"""
    leg_id = get_input("\nEnter Trip Leg ID to update: ")

    for leg in trip_legs:
        if leg['id'] == leg_id:
            print(f"Updating Trip Leg: {leg['start_location']} to {leg['destination']}")

            leg['start_location'] = get_input(f"Starting Location [{leg['start_location']}]: ", True) or leg[
                'start_location']
            leg['destination'] = get_input(f"Destination [{leg['destination']}]: ", True) or leg['destination']
            leg['transport_provider'] = get_input(f"Transport Provider [{leg['transport_provider']}]: ", True) or leg[
                'transport_provider']
            leg['transport_mode'] = get_input(f"Mode of Transport [{leg['transport_mode']}]: ", True) or leg[
                'transport_mode']
            leg['leg_type'] = get_input(f"Leg Type [{leg['leg_type']}]: ", True) or leg['leg_type']

            cost_str = get_input(f"Cost [${leg['cost']}]: ", True)
            if cost_str:
                try:
                    leg['cost'] = int(cost_str)
                except:
                    print("Invalid number. Cost not updated.")

            print("Trip leg updated successfully")
            return

    print(f"Trip leg with ID {leg_id} not found.")


def delete_trip_leg():
    """Delete a trip leg"""
    leg_id = get_input("\nEnter Trip Leg ID to delete: ")

    for i, leg in enumerate(trip_legs):
        if leg['id'] == leg_id:
            # Remove leg reference from trip
            for trip in trips:
                if trip['id'] == leg['trip_id'] and leg['id'] in trip['legs']:
                    trip['legs'].remove(leg['id'])

            del trip_legs[i]
            print(f"Trip leg deleted successfully")
            return

    print(f"Trip leg with ID {leg_id} not found.")

# User management functions

def create_user():
    """Create a new user (coordinator/manager/admin)"""
    print("\n=== Create New User ===")

    role = ""
    while role not in ["coordinator", "manager", "administrator"]:
        role = get_input("Role (coordinator/manager/administrator): ").lower()
        if role not in ["coordinator", "manager", "administrator"]:
            print("Invalid role. Please enter coordinator, manager, or administrator.")

    user = {
        "id": str(uuid.uuid4())[:8],  # Generate a short unique ID
        "username": get_input("Username: "),
        "password": get_input("Password: "),
        "role": role
    }

    users.append(user)
    print(f"{role.capitalize()} '{user['username']}' created successfully with ID: {user['id']}")


def view_users():
    """Display all users"""
    print("\n=== All Users ===")

    if len(users) <= 1:  # Don't count the default admin
        print("No users found.")
        return

    for user in users:
        print(f"ID: {user['id']}")
        print(f"Username: {user['username']}")
        print(f"Role: {user['role']}")
        print("-" * 30)


def delete_user():
    """Delete a user"""
    user_id = get_input("\nEnter User ID to delete: ")

    # Prevent deleting the default admin
    if user_id == "admin1":
        print("Cannot delete the default administrator.")
        return

    for i, user in enumerate(users):
        if user['id'] == user_id:
            username = user['username']
            del users[i]
            print(f"User '{username}' deleted successfully")
            return

    print(f"User with ID {user_id} not found.")

# Trip coordinator functions
def manage_trip_travelers():
    """
    Add or remove travelers from a trip.
    Allows the user to manage the list of travelers associated with a specific trip.
    """
    trip_id = get_input("\nEnter Trip ID: ")  # Prompt the user to enter the Trip ID

    # Find the trip by ID
    trip = None
    for t in trips:
        if t['id'] == trip_id:  # Check if the trip ID matches
            trip = t
            break

    if not trip:  # If the trip is not found, display an error message
        print(f"Trip with ID {trip_id} not found.")
        return

    print(f"\nManaging travelers for trip: {trip['name']}")  # Display the trip name

    while True:
        # Display menu options for managing travelers
        print("\n1. Add traveler to trip")
        print("2. Remove traveler from trip")
        print("3. View travelers on trip")
        print("4. Back to main menu")

        choice = get_input("\nEnter your choice: ")  # Get the user's choice

        if choice == "1":  # Add a traveler to the trip
            traveler_id = get_input("Enter Traveler ID to add: ")  # Prompt for Traveler ID

            # Check if the traveler exists
            traveler_exists = False
            for traveler in travelers:
                if traveler['id'] == traveler_id:  # Check if the traveler ID matches
                    traveler_exists = True
                    break

            if not traveler_exists:  # If the traveler is not found, display an error
                print(f"Traveler with ID {traveler_id} not found.")
                continue

            if traveler_id in trip['travelers']:  # Check if the traveler is already on the trip
                print("Traveler already on this trip.")
            else:
                trip['travelers'].append(traveler_id)  # Add the traveler to the trip
                print("Traveler added to trip successfully.")

        elif choice == "2":  # Remove a traveler from the trip
            traveler_id = get_input("Enter Traveler ID to remove: ")  # Prompt for Traveler ID

            if traveler_id in trip['travelers']:  # Check if the traveler is on the trip
                trip['travelers'].remove(traveler_id)  # Remove the traveler from the trip
                print("Traveler removed from trip successfully.")
            else:
                print("Traveler not found on this trip.")  # Display an error if the traveler is not on the trip

        elif choice == "3":  # View all travelers on the trip
            print("\n=== Travelers on Trip ===")
            if not trip['travelers']:  # Check if there are no travelers on the trip
                print("No travelers on this trip.")
            else:
                for traveler_id in trip['travelers']:  # Iterate through the list of traveler IDs
                    for traveler in travelers:
                        if traveler['id'] == traveler_id:  # Find the traveler by ID
                            print(f"ID: {traveler['id']}")  # Display traveler ID
                            print(f"Name: {traveler['name']}")  # Display traveler name
                            print("-" * 30)  # Separator for readability
                            break

        elif choice == "4":  # Exit the menu
            break

        else:  # Handle invalid input
            print("Invalid choice. Please try again.")

def generate_itinerary():
    """Generate an itinerary for a trip"""
    trip_id = get_input("\nEnter Trip ID: ")

    # Find the trip
    trip = None
    for t in trips:
        if t['id'] == trip_id:
            trip = t
            break

    if not trip:
        print(f"Trip with ID {trip_id} not found.")
        return

    print(f"\n=== Itinerary for {trip['name']} ===")
    print(f"Start Date: {trip['start_date'].strftime('%d/%m/%Y')}")
    print(f"Duration: {trip['duration']} days")
    print(f"Contact: {trip['contact']}")

    # Get trip legs for this trip
    trip_legs_for_trip = [leg for leg in trip_legs if leg['trip_id'] == trip_id]

    if not trip_legs_for_trip:
        print("\nNo trip legs defined for this trip.")
    else:
        print("\nTrip Legs:")
        for leg in trip_legs_for_trip:
            print(f"- {leg['start_location']} to {leg['destination']} ({leg['transport_mode']})")
            print(f"  Type: {leg['leg_type']}, Cost: ${leg['cost']}")

    # Calculate total cost
    total_cost = sum(leg['cost'] for leg in trip_legs_for_trip)
    print(f"\nTotal Trip Cost: ${total_cost}")

# Reporting and analytics functions
def generate_financial_report():
    """Generate a financial report showing costs by trip"""
    print("\n=== Financial Report ===")

    if not trips:
        print("No trips found.")
        return

    # Calculate costs for each trip
    trip_costs = {}
    for trip in trips:
        trip_id = trip['id']
        trip_name = trip['name']

        # Get legs for this trip
        legs_for_trip = [leg for leg in trip_legs if leg['trip_id'] == trip_id]
        total_cost = sum(leg['cost'] for leg in legs_for_trip)

        trip_costs[trip_name] = total_cost

    # Display financial report
    print("\nTrip Costs:")
    for trip_name, cost in trip_costs.items():
        print(f"{trip_name}: ${cost}")

    # Calculate total revenue
    total_revenue = sum(trip_costs.values())
    print(f"\nTotal Revenue: ${total_revenue}")

    # Create a simple bar chart
    if trip_costs:
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(trip_costs.keys(), trip_costs.values())
            plt.title('Trip Costs')
            plt.xlabel('Trip Name')
            plt.ylabel('Cost ($)')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig('trip_costs.png')
            plt.close()
            print("Chart saved as 'trip_costs.png'")
        except Exception as e:
            print(f"Could not generate chart: {e}")
            print("Make sure matplotlib is installed or use 'pip install matplotlib'")


def generate_traveler_report():
    """Generate a report showing traveler statistics"""
    print("\n=== Traveler Statistics ===")

    if not travelers:
        print("No travelers found.")
        return

    # Count travelers by trip
    travelers_per_trip = {}
    for trip in trips:
        travelers_per_trip[trip['name']] = len(trip['travelers'])

    # Display traveler statistics
    print("\nNumber of Travelers per Trip:")
    for trip_name, count in travelers_per_trip.items():
        print(f"{trip_name}: {count} travelers")

    # Total number of travelers
    print(f"\nTotal Travelers: {len(travelers)}")

    # Create a simple pie chart
    if travelers_per_trip:
        try:
            plt.figure(figsize=(8, 8))
            plt.pie(travelers_per_trip.values(), labels=travelers_per_trip.keys(), autopct='%1.1f%%')
            plt.title('Travelers by Trip')
            plt.tight_layout()
            plt.savefig('travelers_by_trip.png')
            plt.close()
            print("Chart saved as 'travelers_by_trip.png'")
        except Exception as e:
            print(f"Could not generate chart: {e}")
            print("Make sure matplotlib is installed or use 'pip install matplotlib'")


def generate_trip_performance_report():
    """Generate a report showing trip performance metrics"""
    print("\n=== Trip Performance Report ===")

    if not trips:
        print("No trips found.")
        return

    # Calculate metrics for each trip
    for trip in trips:
        trip_id = trip['id']
        trip_name = trip['name']

        # Get legs for this trip
        legs_for_trip = [leg for leg in trip_legs if leg['trip_id'] == trip_id]

        # Calculate metrics
        total_cost = sum(leg['cost'] for leg in legs_for_trip)
        num_travelers = len(trip['travelers'])
        num_legs = len(legs_for_trip)

        # Calculate cost per traveler (avoid division by zero)
        cost_per_traveler = total_cost / num_travelers if num_travelers > 0 else 0

        print(f"\nTrip: {trip_name}")
        print(f"Total Cost: ${total_cost}")
        print(f"Number of Travelers: {num_travelers}")
        print(f"Number of Trip Legs: {num_legs}")
        print(f"Cost per Traveler: ${cost_per_traveler:.2f}")
        print("-" * 30)

    # Analyze transport modes
    if trip_legs:
        transport_modes = Counter([leg['transport_mode'] for leg in trip_legs])

        print("\nTransport Mode Usage:")
        for mode, count in transport_modes.items():
            print(f"{mode}: {count} times")

        # Create a simple bar chart for transport modes
        try:
            plt.figure(figsize=(8, 6))
            plt.bar(transport_modes.keys(), transport_modes.values())
            plt.title('Transport Mode Usage')
            plt.xlabel('Transport Mode')
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig('transport_modes.png')
            plt.close()
            print("Chart saved as 'transport_modes.png'")
        except Exception as e:
            print(f"Could not generate chart: {e}")
            print("Make sure matplotlib is installed or use 'pip install matplotlib'")

# Menu functions
def reporting_menu():
    """
    Display the reporting and analytics menu.
    Allows the user to generate various reports or return to the main menu.
    """
    while True:
        # Display menu options
        print("\n=== Reporting and Analytics ===")
        print("1. Financial Report")  # Option to generate a financial report
        print("2. Traveler Statistics")  # Option to generate traveler statistics
        print("3. Trip Performance Report")  # Option to generate trip performance metrics
        print("4. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            generate_financial_report()  # Call function to generate financial report
        elif choice == "2":
            generate_traveler_report()  # Call function to generate traveler statistics
        elif choice == "3":
            generate_trip_performance_report()  # Call function to generate trip performance metrics
        elif choice == "4":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def display_main_menu():
    """
    Display the main menu options for the travel management system.
    Provides access to various management and reporting functions.
    """
    print("\n=== Travel Management System ===")
    print("1. Trip Management")  # Access trip management functions
    print("2. Traveler Management")  # Access traveler management functions
    print("3. Trip Leg Management")  # Access trip leg management functions
    print("4. Trip Coordinator Functions")  # Access trip coordinator functions
    print("5. Trip Manager Functions")  # Access trip manager functions
    print("6. Administrator Functions")  # Access administrator functions
    print("7. Reporting and Analytics")  # Access reporting and analytics functions
    print("8. Exit")  # Exit the program


def trip_management_menu():
    """
    Display the trip management menu.
    Allows the user to create, view, update, or delete trips, or return to the main menu.
    """
    while True:
        # Display menu options
        print("\n=== Trip Management ===")
        print("1. Create Trip")  # Option to create a new trip
        print("2. View All Trips")  # Option to view all trips
        print("3. Update Trip")  # Option to update an existing trip
        print("4. Delete Trip")  # Option to delete a trip
        print("5. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            create_trip()  # Call function to create a new trip
        elif choice == "2":
            view_trips()  # Call function to view all trips
        elif choice == "3":
            update_trip()  # Call function to update an existing trip
        elif choice == "4":
            delete_trip()  # Call function to delete a trip
        elif choice == "5":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def traveler_management_menu():
    """
    Display the traveler management menu.
    Allows the user to create, view, update, or delete travelers, or return to the main menu.
    """
    while True:
        # Display menu options
        print("\n=== Traveler Management ===")
        print("1. Create Traveler")  # Option to create a new traveler
        print("2. View All Travelers")  # Option to view all travelers
        print("3. Update Traveler")  # Option to update an existing traveler
        print("4. Delete Traveler")  # Option to delete a traveler
        print("5. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            create_traveler()  # Call function to create a new traveler
        elif choice == "2":
            view_travelers()  # Call function to view all travelers
        elif choice == "3":
            update_traveler()  # Call function to update an existing traveler
        elif choice == "4":
            delete_traveler()  # Call function to delete a traveler
        elif choice == "5":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def trip_leg_management_menu():
    """
    Display the trip leg management menu.
    Allows the user to create, view, update, or delete trip legs, or return to the main menu.
    """
    while True:
        # Display menu options
        print("\n=== Trip Leg Management ===")
        print("1. Create Trip Leg")  # Option to create a new trip leg
        print("2. View All Trip Legs")  # Option to view all trip legs
        print("3. Update Trip Leg")  # Option to update an existing trip leg
        print("4. Delete Trip Leg")  # Option to delete a trip leg
        print("5. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            create_trip_leg()  # Call function to create a new trip leg
        elif choice == "2":
            view_trip_legs()  # Call function to view all trip legs
        elif choice == "3":
            update_trip_leg()  # Call function to update an existing trip leg
        elif choice == "4":
            delete_trip_leg()  # Call function to delete a trip leg
        elif choice == "5":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def trip_coordinator_menu():
    """
    Display the trip coordinator menu.
    Allows the user to manage trip travelers, generate itineraries, or return to the main menu.
    """
    while True:
        # Display menu options
        print("\n=== Trip Coordinator Functions ===")
        print("1. Manage Trip Travelers")  # Option to manage travelers for a trip
        print("2. Generate Trip Itinerary")  # Option to generate a trip itinerary
        print("3. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            manage_trip_travelers()  # Call function to manage trip travelers
        elif choice == "2":
            generate_itinerary()  # Call function to generate a trip itinerary
        elif choice == "3":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def trip_manager_menu():
    """
    Display the trip manager menu.
    Allows the user to manage trip coordinators or access coordinator functions.
    """
    while True:
        # Display menu options
        print("\n=== Trip Manager Functions ===")
        print("1. Create Trip Coordinator")  # Option to create a new trip coordinator
        print("2. View Trip Coordinators")  # Option to view all trip coordinators
        print("3. Delete Trip Coordinator")  # Option to delete a trip coordinator
        print("4. Access Trip Coordinator Functions")  # Option to access coordinator functions
        print("5. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            # Create a new trip coordinator
            print("\n=== Create New Trip Coordinator ===")
            user = {
                "id": str(uuid.uuid4())[:8],  # Generate a short unique ID
                "username": get_input("Username: "),  # Get username
                "password": get_input("Password: "),  # Get password
                "role": "coordinator"  # Assign role as coordinator
            }
            users.append(user)  # Add the new user to the users list
            print(f"Trip Coordinator '{user['username']}' created successfully with ID: {user['id']}")

        elif choice == "2":
            # View all trip coordinators
            print("\n=== Trip Coordinators ===")
            coordinators = [user for user in users if user['role'] == 'coordinator']  # Filter coordinators
            if not coordinators:
                print("No trip coordinators found.")  # Handle no coordinators
            else:
                for user in coordinators:
                    print(f"ID: {user['id']}")
                    print(f"Username: {user['username']}")
                    print("-" * 30)

        elif choice == "3":
            # Delete a trip coordinator
            user_id = get_input("\nEnter Trip Coordinator ID to delete: ")
            for i, user in enumerate(users):
                if user['id'] == user_id and user['role'] == 'coordinator':
                    username = user['username']
                    del users[i]  # Remove the user from the list
                    print(f"Trip Coordinator '{username}' deleted successfully")
                    break
            else:
                print(f"Trip Coordinator with ID {user_id} not found.")  # Handle invalid ID

        elif choice == "4":
            trip_coordinator_menu()  # Access trip coordinator functions

        elif choice == "5":
            break  # Exit the menu and return to the main menu

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


def admin_menu():
    """
    Display the administrator menu.
    Allows the user to manage users or access trip manager functions.
    """
    while True:
        # Display menu options
        print("\n=== Administrator Functions ===")
        print("1. Create User (Coordinator/Manager)")  # Option to create a new user
        print("2. View All Users")  # Option to view all users
        print("3. Delete User")  # Option to delete a user
        print("4. Access Trip Manager Functions")  # Option to access trip manager functions
        print("5. Back to Main Menu")  # Option to return to the main menu

        # Get user input
        choice = get_input("\nEnter your choice: ")

        # Handle user input
        if choice == "1":
            create_user()  # Call function to create a new user
        elif choice == "2":
            view_users()  # Call function to view all users
        elif choice == "3":
            delete_user()  # Call function to delete a user
        elif choice == "4":
            trip_manager_menu()  # Access trip manager functions
        elif choice == "5":
            break  # Exit the menu and return to the main menu
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input


# Login system
def login():
    """
    User login function.
    Prompts the user for a username and password, checks the credentials against the `users` list,
    and returns the user object if authentication is successful.
    """
    print("\n=== Login ===")
    username = get_input("Username: ")  # Prompt the user to enter their username
    password = get_input("Password: ")  # Prompt the user to enter their password

    # Iterate through the list of users to find a matching username and password
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Welcome, {username}!")  # Display a welcome message for the authenticated user
            return user  # Return the authenticated user object

    # If no match is found, display an error message
    print("Invalid username or password.")
    return None  # Return None to indicate failed login


# Main function
def main():
    """
    Main function to run the program.
    Handles user authentication and provides access to various system menus based on the user's role.
    """
    print("Welcome to the Simple Travel Management System")  # Display a welcome message

    user = None
    # Loop until the user successfully logs in
    while not user:
        user = login()  # Call the login function to authenticate the user

    role = user['role']  # Retrieve the role of the authenticated user

    # Main program loop
    while True:
        display_main_menu()  # Display the main menu options
        choice = get_input("\nEnter your choice: ")  # Prompt the user to select a menu option

        # Handle the user's menu choice
        if choice == "1":  # Trip Management
            trip_management_menu()  # Access the trip management menu

        elif choice == "2":  # Traveler Management
            traveler_management_menu()  # Access the traveler management menu

        elif choice == "3":  # Trip Leg Management
            trip_leg_management_menu()  # Access the trip leg management menu

        elif choice == "4":  # Trip Coordinator Functions
            # Check if the user has the required role to access this menu
            if role in ["coordinator", "manager", "administrator"]:
                trip_coordinator_menu()  # Access the trip coordinator menu
            else:
                print("Access denied. You need to be a Trip Coordinator or higher.")  # Display an access denied message

        elif choice == "5":  # Trip Manager Functions
            # Check if the user has the required role to access this menu
            if role in ["manager", "administrator"]:
                trip_manager_menu()  # Access the trip manager menu
            else:
                print("Access denied. You need to be a Trip Manager or Administrator.")  # Display an access denied message

        elif choice == "6":  # Administrator Functions
            # Check if the user has the required role to access this menu
            if role == "administrator":
                admin_menu()  # Access the administrator menu
            else:
                print("Access denied. You need to be an Administrator.")  # Display an access denied message

        elif choice == "7":  # Reporting and Analytics
            # Check if the user has the required role to access this menu
            if role in ["manager", "administrator"]:
                reporting_menu()  # Access the reporting and analytics menu
            else:
                print("Access denied. You need to be a Trip Manager or Administrator.")  # Display an access denied message

        elif choice == "8":  # Exit
            print("Thank you for using the Travel Management System. Goodbye!")  # Display a goodbye message
            break  # Exit the program loop

        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu input

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program

