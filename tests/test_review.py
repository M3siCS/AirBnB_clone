import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        review = Review(text="Great place!")
        self.assertEqual(review.text, "Great place!")

if __name__ == "__main__":
    unittest.main()

