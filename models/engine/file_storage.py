#!/usr/bin/python3
"""File Storage for AirBnB Clone"""
import json
from os.path import exists


class FileStorage:
    """Class for FileStorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets obj in __objects with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serialize __objects to JSON file"""
        temp = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(temp, jsonfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                decereal = json.load(jsonfile)
            for key, value in decereal.items():
                cls_name = value['__class__']
                cls = globals().get(cls_name)
                if cls:
                    self.__objects[key] = cls(**value)

