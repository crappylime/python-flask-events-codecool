import sqlite3


class Database:
    """Class representing database."""

    @classmethod
    def create_db(cls, filename):
        # Open and read the file as a single buffer

        with open(filename, 'r') as f:
            sqlfile = f.read()

        conn = sqlite3.connect('events.db')
        with conn:
            cur = conn.cursor()
            cur.execute(sqlfile)

    @classmethod
    def execute_query(cls, query, args):
        """Execute query and return data"""
        conn = sqlite3.connect('events.db')
        cur = conn.cursor()
        cur.execute(query, args)
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data
