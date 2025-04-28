# data storage is complete by using simple lists instead of a database
# 'trips' stores details from trips
# 'travellers' stores details from travellers
# 'trip_legs' stores details of each individual trip leg
# 'users' stores user accounts
trips = []
travelers = []
trip_legs = []
users = []

# trip management functions

def create_trip():
    """
        This Creates a new trip and adds it to the `trips` list.
        """
    print("\n=== Create New Trip ===")

    # Collect trip details from the user
    trip = {
        "id": str(uuid.uuid4())[:8],  # Generates a short unique ID for the trip
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

        if not trips:  # Check if there are no trips and return message if none found.
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

                trip['coordinator'] = get_input(f"Trip Coordinator ID [{trip['coordinator']}]: ", True) or trip[
                    'coordinator']
                trip['contact'] = get_input(f"Contact Information [{trip['contact']}]: ", True) or trip['contact']

                print(f"Trip '{trip['name']}' updated successfully")
                return

        print(f"Trip with ID {trip_id} not found.")  # If no trip matches the given ID produce an error message

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

        print(f"Trip with ID {trip_id} not found.")  # If no trip matches the given ID produce error message


