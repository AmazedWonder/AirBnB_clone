#!/usr/bin/python3

from models.base_model import BaseModel


# class City(BaseModel):
#     state_id = ""
#     name = ""

class City(BaseModel):
    def __init__(self):
        super().__init__()
        self.state_id = ""
        self.name = ""
