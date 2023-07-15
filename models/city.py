#!/usr/bin/python3
"""Define the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the city class
    Attributes:
    state_id (string): empty string will be State.id.
    name (string): empty string(the name of the city).
    """

    state_id = ""
    name = ""
