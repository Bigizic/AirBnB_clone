#!/usr/bin/python3
""" Class Module
A class BaseModel that defines all common attributes/methods for other
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
class BaseModel:
    """Main Class
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        dct = str(self.__dict__)
        cla = self.__class__.__name__
        return ("[{}] ({}) {}" .format(cla, self.id, dct))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created-at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
