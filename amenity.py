#!/usr/bin/python3

from models.base_model import BaseModel


# class Amenity(BaseModel):
#     name = ""

class Amenity(BaseModel):
    def __init__(self):
        super().__init__()
        self.name = ""