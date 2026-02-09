#!/usr/bin/python3
"""Defines the User model."""
from models.base_model import BaseModel


class User(BaseModel):
    """class user that inhirets from BAseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
