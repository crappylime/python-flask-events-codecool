from database import Database


class Event:
    """ Class representing event."""

    def __init__(self, name, date, description, id=None):
        self.name = name
        self.date = date
        self.description = description
        self.id = id

    @classmethod
    def get_all(cls):
        """ Retrieves all events from database and returns them as list.
        Returns:
            list(Event): list of all events
        """
        events_list = []
        query = "SELECT * FROM `events` ORDER BY date DESC;"
        data = Database.execute_query(query, ())

        for row in data:
            events_list.append(cls(row[1], row[2], row[3], row[0]))
        return events_list

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves event with given id from database.
        Args:
            id(int): event id
        Returns:
            Event: Event object with a given id
        """
        query = "SELECT * FROM `events` WHERE `id` = ?;"
        rows = Database.execute_query(query, (id,))
        row = rows[0]
        if row:
            return cls(row[1], row[2], row[3], row[0])

    def save(self):
        """ Saves/updates event in database """
        if self.id:
            query = "UPDATE `events` SET `name` = ?, `date` = ?, `description` = ? WHERE `id` = ?;"
            Database.execute_query(query, (self.name, self.date, self.description, self.id))
        else:
            query = 'INSERT INTO events (`name`, `date`, `description`) VALUES (?, ?, ?);'
            Database.execute_query(query, (self.name, self.date, self.description))

    def delete(self):
        """ Removes event from the database """
        query = "DELETE FROM events WHERE id = ?;"
        Database.execute_query(query, (self.id,))
