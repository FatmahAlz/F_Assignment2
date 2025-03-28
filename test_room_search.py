import unittest
from classes import Hotel, Room
from datetime import date, timedelta

class TestRoomSearch(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Grand Plaza", "New York", 5, 150)
        self.room1 = Room(101, "Standard", ["TV", "WiFi"], 150.00, True)
        self.room2 = Room(102, "Deluxe", ["TV", "Mini-bar"], 250.00, False)
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)

    def test_find_available_rooms(self):
        """Test finding all available rooms"""
        available = [room for room in self.hotel.roomList if room.get_availability_status()]
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].room_number, 101)

    def test_search_by_room_type(self):
        """Test searching by room type"""
        deluxe_rooms = [room for room in self.hotel.roomList
                       if room.get_room_type() == "Deluxe"]
        self.assertEqual(len(deluxe_rooms), 1)

if __name__ == '__main__':
    unittest.main()