import os
import urllib.parse as urlparse

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database:
    """Class representing database."""

    @classmethod
    def get_connection(cls):
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn


    @classmethod
    def create_db(cls, filename):
        # Open and read the file as a single buffer

        with open(filename, 'r') as f:
            sqlfile = f.read()

        conn = Database.get_connection()
        with conn:
            cur = conn.cursor()
            cur.execute(sqlfile)

    @classmethod
    def execute_query(cls, query, args):
        """Execute query and return data"""
        conn = Database.get_connection()
        cur = conn.cursor()
        cur.execute(query, args)
        data = cur.fetchall()
        conn.commit()
        conn.close()
        return data
