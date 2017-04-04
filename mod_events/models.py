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

    def save(self):
        """ Saves/updates event in database """
        if self.id:
            query = "UPDATE `events` SET `name` = ?, `date` = ?, `description` = ? WHERE `id` = ?;"
            Database.execute_query(query, (self.name, self.date, self.description, self.id))
        else:
            query = 'INSERT INTO events (`name`, `date`, `description`) VALUES (?, ?, ?);'
            Database.execute_query(query, (self.name, self.date, self.description))
