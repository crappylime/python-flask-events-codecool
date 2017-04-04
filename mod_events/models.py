from database import Database


class Event:
    """ Class representing event."""

    def __init__(self, name, date, description, id=None):
        self.name = name
        self.date = date
        self.description = description
        self.id = id
