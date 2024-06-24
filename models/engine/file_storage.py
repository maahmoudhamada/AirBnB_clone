#!/usr/bin/python3
"""FileStorage class Module"""

import json


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def classSelector(self, inst, flag):
        """Method to choose the correct class"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.review import Review

        classess = [BaseModel, User, Amenity, Place, State, City, Review]
        if flag == 1:
            if type(inst) in classess:
                for _cls in classess:
                    if type(inst) is _cls:
                        return _cls
        else:
            for _cls in classess:
                if inst['__class__'] == _cls.__name__:
                    return _cls
        return None

    def instance_converter(self, flag):
        """Method to convert instance to dict, vise verca"""
        new_dict = self.__objects.copy()

        if flag == 1:
            for key in new_dict.keys():
                _cls = self.classSelector(new_dict[key], 1)
                if isinstance(new_dict[key], _cls) and _cls:
                    new_dict.update({key: new_dict[key].to_dict()})
            return new_dict
        else:
            for key in new_dict.keys():
                _cls = self.classSelector(new_dict[key], 2)
                if isinstance(new_dict[key], dict):
                    new_dict.update({key: _cls(**new_dict[key])})
            self.__objects = new_dict.copy()

    def all(self):
        """Method to return dict containing all objects created"""
        return self.__objects

    def new(self, obj):
        """Method to add new objects to dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """Method to save objects into a file"""
        new_dict = self.instance_converter(1)
        with open(self.__file_path, "w+", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Method to recover objects created before"""
        try:
            with open(self.__file_path, "r+", encoding="utf-8") as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
        self.instance_converter(2)
