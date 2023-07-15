#!/usr/bin/python3
"""A subclass Module
 a class User that inherits from BaseModel

 args:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string

Raises:
    None

Return:
    Void
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Subclass of BaseModel implementation
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
