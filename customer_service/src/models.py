# # models.py

from flask_pymongo import PyMongo
import pymongo

mongo = PyMongo()

class Customer:
    def __init__(self, first_name, last_name, middle_name=None, age=None, nationality=None, sex=None, income=None, education_level=None, position=None):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("First name must be a non-empty string")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("Last name must be a non-empty string")

        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.nationality = nationality
        self.sex = sex
        self.income = income
        self.education_level = education_level
        self.position = position

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                if key == "last_name" and (not isinstance(value, str) or not value):
                    raise ValueError("Last name must be a non-empty string")
                if key == "first_name" and (not isinstance(value, str) or not value):
                    raise ValueError("Last name must be a non-empty string")
                setattr(self, key, value)

    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'age': self.age,
            'nationality': self.nationality,
            'sex': self.sex,
            'income': self.income,
            'education_level': self.education_level,
            'position': self.position
        }


