import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_initialization(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

if __name__ == "__main__":
    unittest.main()

