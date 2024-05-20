import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_base_model_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

