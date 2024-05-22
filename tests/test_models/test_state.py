import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attributes(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")

if __name__ == "__main__":
    unittest.main()

