#!/usr/bin/python3
"""file containing basemodel class"""
from datetime import datetime
from models import storage
import uuid

class BaseModel():
    """Class BaseModel, base model for AirBnB Clone"""

    def __init__(self, *args, **kwargs):
        """initializes BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in {'created_at', 'updated_at'}:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """class str method"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary of BaseModel"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

