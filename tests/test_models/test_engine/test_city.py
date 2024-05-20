import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_initialization(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_attributes(self):
        city = City(name="San Francisco", state_id="CA")
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "CA")

if __name__ == "__main__":
    unittest.main()

