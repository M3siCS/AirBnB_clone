#!/usr/bin/python3
"""File Storage for AirBnB Clone"""
import json
from models.base_model import BaseModel
from models.user import User
from os.path import exists


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value['__class__']
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def classes(self):
        return {"BaseModel": BaseModel, "User": User}
