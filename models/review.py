#!/usr/bin/python3
"""Define the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent the review class
    Attributes:
    place_id (string): empty string will be Place.id.
    user_id (string): empty string will be User.id.
    text (string): empty string(the review of the user).
    """

    place_id = ""
    user_id = ""
    text = ""
