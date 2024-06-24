#!/usr/bin/python3
"""FileStorage class Module"""

import json


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def classSelector(self, inst, flag):
        from models.base_model import BaseModel
        from models.user import User
        classess = [BaseModel, User]
        if flag == 1:
            if type(inst) in classess:
                for cl in classess:
                    if type(inst) is cl:
                        return cl
        else:
            for cl in classess:
                if inst['__class__'] == cl.__name__:
                    return cl
        return None

    def instance_converter(self, flag):
        """Method to convert instance to dict, vise verca"""
        from models.base_model import BaseModel
        new_dict = self.__objects.copy()

        if flag == 1:
            for key in new_dict.keys():
                cl = self.classSelector(new_dict[key], 1)
                if isinstance(new_dict[key], cl):
                    new_dict.update({key: new_dict[key].to_dict()})
            return new_dict
        else:
            for key in new_dict.keys():
                cl = self.classSelector(new_dict[key], 2)
                if isinstance(new_dict[key], dict):
                    new_dict.update({key: cl(**new_dict[key])})
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
