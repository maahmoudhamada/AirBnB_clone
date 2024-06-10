#!/usr/bin/python3
"""FileStorage class Module"""

import json


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def instance_converter(self, flag):
        """Method to convert instance to dict, vise verca"""
        from models.base_model import BaseModel
        new_dict = self.__objects.copy()

        if flag == 1:
            for key in new_dict.keys():
                if isinstance(new_dict[key], BaseModel):
                    new_dict.update({key: new_dict[key].to_dict()})
            return new_dict
        else:
            for key in new_dict.keys():
                if isinstance(new_dict[key], dict):
                    new_dict.update({key: BaseModel(**new_dict[key])})
            self.__objects = new_dict.copy()

    def all(self):
        """Method to return dict containing all objects created"""
        """Method to return all saved objcs"""
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
