from flask import Flask
from mod_events.controllers import mod_events
from database import Database
import os

app = Flask(__name__)
app.register_blueprint(mod_events)
app.secret_key = os.urandom(24)

Database.create_db('/home/lama/Code/Python/python-flask-events-codecool/database.sql')

if __name__ == "__main__":
    app.run()
