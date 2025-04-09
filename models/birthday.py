from models.field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
