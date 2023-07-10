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

class BaseModel:
    """Main Class
    """

    def __init__(self):
        self.id = uuid
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return("[{}] ({}) {{}}"
                .format(self.__class__.__name__ , self.id, self.__dict__))

    def save(self):
        self.updated_at = current_date_time

    def to_dict(self):
        return
        
