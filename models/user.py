from enum import Enum

class Role(Enum):
    ADMIN = 1
    SELLER = 2
    BUYER = 3

class User():

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role