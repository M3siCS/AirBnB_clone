import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_file_storage_instance(self):
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

