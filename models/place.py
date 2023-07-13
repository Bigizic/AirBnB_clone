#!/usr/bin/python3
"""Define the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent the place class
    Attributes:
    city_id (string): empty string will be City.id.
    user_id (string): empty string will be User.id.
    name (string): empty string(name of the place).
    description (string): empty string(where the place).
    number_rooms (int): 0.
    number_bathrooms (int): 0.
    max_guest (int): 0.
    price_by_night (int): 0.
    latitude (float): 0.0.
    longitude (float): 0.0.
    amenity_ids (list of strings): empty listwill be Amenity.id.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
