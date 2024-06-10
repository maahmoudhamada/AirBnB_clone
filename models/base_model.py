#!/usr/bin/python3
"""BaseModel Module"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel Class"""

    # =========================== Date_converter ======================

    def date_converter(self, flag, key="", value=""):
        """Method to convert date from to isoformat"""
        if flag == 1:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            setattr(self, key, datetime.fromisoformat(value))

    # =========================== Init ================================

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if args:
            pass
        elif kwargs and kwargs != {}:
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    self.date_converter(2, key, kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid4())
            self.date_converter(1)
            storage.new(self)

    # =========================== Str ================================

    def __str__(self):
        """Mehtod to return unformal string repr. for an instance"""
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)

    # =========================== Save ==============================

    def save(self):
        """Method to update updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    # =========================== to_dict ===========================

    def to_dict(self):
        """Method to return a copy from an instance dict"""
        new_dict = self.__dict__.copy()
        crtd_at = new_dict['created_at'].isoformat()
        uptd_at = new_dict['updated_at'].isoformat()
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict.update({'created_at': crtd_at})
        new_dict.update({'updated_at': uptd_at})
        return new_dict
