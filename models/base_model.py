#!/usr/bin/python3
""" Class Module
A class BaseModel that defines all common
attributes/methods for other
classes.

Args:
    None

Raises:
    None

Return:
    void
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Main Class

    BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns dict format, class name and unique id
        """
        dct = str(self.__dict__)
        cla = self.__class__.__name__
        return ("[{}] ({}) {}" .format(cla, self.id, dct))

    def save(self):
        """Update updated_at public instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns self.__dict__,
        sets object class to class name,
        converts created_at and updated_at to  string obj in
        ISO format
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
