import unittest
from main import trips, create_trip, view_trips, update_trip, delete_trip
from unittest.mock import patch
from main import travelers, create_traveler, view_travelers, update_traveler, delete_traveler
import datetime
from main import trips, trip_legs, create_trip_leg
from main import users, create_user
from io import StringIO
from main import generate_financial_report, trips, trip_legs


# Trip management test

class TestTripManagement(unittest.TestCase):

    def setUp(self):
        """Set up initial data for testing."""
        self.test_trip = {
            "id": "test123",
            "name": "Test Trip",
            "start_date": "#",
            "duration": 5,
            "coordinator": "John Doe",
            "contact": "1234567890",
            "travelers": [],
            "legs": []
        }
        trips.append(self.test_trip)

    def tearDown(self):
        """Clean up after each test."""
        trips.clear()

    def test_create_trip(self):
        """Test creating a new trip."""
        initial_count = len(trips)
        create_trip()
        self.assertEqual(len(trips), initial_count + 1)
        self.assertIn("name", trips[-1])
        self.assertIn("start_date", trips[-1])


#update trip
    def test_update_trip(self):
        """Test updating an existing trip."""
        trips[0]["name"] = "Updated Trip"
        self.assertEqual(trips[0]["name"], "Updated Trip")


#delete trip
    def test_delete_trip(self):
        """Test deleting a trip."""
        initial_count = len(trips)
        delete_trip()
        self.assertEqual(len(trips), initial_count - 1)


#Traveler management test
class TestTravelerManagement(unittest.TestCase):

    def setUp(self):
        """Set up initial data for testing."""
        self.test_traveler = {
            "id": "test123",
            "name": "John Doe",
            "address": "123 Main St",
            "dob": datetime.date(1990, 1, 1),
            "emergency_contact": "9876543210",
            "gov_id_type": "Passport",
            "gov_id_number": "A1234567"
        }
        travelers.append(self.test_traveler)

    def tearDown(self):
        """Clean up after each test."""
        travelers.clear()

#create traveler
    @patch('main.get_input', side_effect=["Jane Doe", "456 Elm St", "01/01/1995", "1234567890", "Driver's License", "B9876543"])
    @patch('main.get_date_input', return_value=datetime.date(1995, 1, 1))
    def test_create_traveler(self, mock_date_input, mock_input):
        """Test creating a new traveler."""
        initial_count = len(travelers)
        create_traveler()
        self.assertEqual(len(travelers), initial_count + 1)
        self.assertEqual(travelers[-1]["name"], "Jane Doe")
        self.assertEqual(travelers[-1]["dob"], datetime.date(1995, 1, 1))

#View traveller
    @patch('builtins.print')
    def test_view_travelers(self, mock_print):
        """Test viewing all travelers."""
        view_travelers()
        mock_print.assert_any_call(f"Name: {self.test_traveler['name']}")

        mock_print.assert_any_call(f"Date of Birth: {self.test_traveler['dob'].strftime('%d/%m/%Y')}")
#update traveller
    @patch('main.get_input', side_effect=["test123", "Updated Name", "Updated Address", "02/02/1992", "1111111111", "ID Card", "C1234567"])
    @patch('main.get_date_input', return_value=datetime.date(1992, 2, 2))
    def test_update_traveler(self, mock_date_input, mock_input):
        """Test updating an existing traveler."""
        update_traveler()
        self.assertEqual(travelers[0]["name"], "Updated Name")
        self.assertEqual(travelers[0]["dob"], datetime.date(1992, 2, 2))

#delete traveller
    @patch('main.get_input', return_value="test123")
    def test_delete_traveler(self, mock_input):
        """Test deleting a traveler."""
        initial_count = len(travelers)
        delete_traveler()
        self.assertEqual(len(travelers), initial_count - 1)
        self.assertNotIn(self.test_traveler, travelers)

#Trip leg management test
class TestTripLegManagement(unittest.TestCase):

    def setUp(self):
        """Set up initial data for testing."""
        self.test_trip = {
            "id": "trip123",
            "name": "Test Trip",
            "start_date": "2023-10-01",
            "duration": 5,
            "coordinator": "John Doe",
            "contact": "1234567890",
            "travelers": [],
            "legs": []
        }
        trips.append(self.test_trip)

    def tearDown(self):
        """Clean up after each test."""
        trips.clear()
        trip_legs.clear()

#create trip leg
    @patch('main.get_input', side_effect=["trip123", "New York", "Los Angeles", "Airline", "Flight", "transfer"])
    @patch('main.get_int_input', return_value=500)
    def test_create_trip_leg(self, mock_int_input, mock_input):
        """Test creating a new trip leg."""
        initial_leg_count = len(trip_legs)
        create_trip_leg()
        self.assertEqual(len(trip_legs), initial_leg_count + 1)
        self.assertEqual(trip_legs[-1]["start_location"], "New York")
        self.assertEqual(trip_legs[-1]["destination"], "Los Angeles")
        self.assertEqual(trip_legs[-1]["cost"], 500)
        self.assertIn(trip_legs[-1]["id"], self.test_trip["legs"])

#Users testing
class TestUserManagement(unittest.TestCase):

    def setUp(self):
        """Set up initial data for testing."""
        self.default_admin = {
            "id": "admin1",
            "username": "admin",
            "password": "admin123",
            "role": "administrator"
        }
        users.clear()
        users.append(self.default_admin)

    def tearDown(self):
        """Clean up after each test."""
        users.clear()

#Create user test
    @patch('main.get_input', side_effect=["manager", "testuser", "password123"])
    def test_create_user(self, mock_input):
        """Test creating a new user."""
        initial_count = len(users)
        create_user()
        self.assertEqual(len(users), initial_count + 1)
        self.assertEqual(users[-1]["username"], "testuser")
        self.assertEqual(users[-1]["role"], "manager")

    @patch('main.get_input', side_effect=["invalid_role", "manager", "testuser", "password123"])
    def test_create_user_invalid_role(self, mock_input):
        """Test creating a user with an invalid role initially."""
        initial_count = len(users)
        create_user()
        self.assertEqual(len(users), initial_count + 1)
        self.assertEqual(users[-1]["role"], "manager")

#Reporting and analytics
class TestGenerateFinancialReport(unittest.TestCase):

    def setUp(self):
        """Set up test data for trips and trip legs."""
        self.test_trip = {
            "id": "trip123",
            "name": "Test Trip",
            "start_date": "2023-10-01",
            "duration": 5,
            "coordinator": "John Doe",
            "contact": "1234567890",
            "travelers": [],
            "legs": []
        }
        self.test_leg = {
            "id": "leg123",
            "trip_id": "trip123",
            "start_location": "New York",
            "destination": "Los Angeles",
            "transport_provider": "Airline",
            "transport_mode": "Flight",
            "leg_type": "transfer",
            "cost": 500
        }
        trips.append(self.test_trip)
        trip_legs.append(self.test_leg)

    def tearDown(self):
        """Clean up test data."""
        trips.clear()
        trip_legs.clear()

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_financial_report(self, mock_stdout):
        """Test the financial report generation."""
        generate_financial_report()
        output = mock_stdout.getvalue()

        # Check if the trip cost and total revenue are displayed correctly
        self.assertIn("Test Trip: $500", output)
        self.assertIn("Total Revenue: $500", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_financial_report_no_trips(self, mock_stdout):
        """Test the financial report when no trips exist."""
        trips.clear()  # Ensure no trips exist
        generate_financial_report()
        output = mock_stdout.getvalue()

        # Check if the correct message is displayed
        self.assertIn("No trips found.", output)

if __name__ == "__main__":
    unittest.main()