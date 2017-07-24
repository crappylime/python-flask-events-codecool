import os

from flask import Flask, redirect, url_for

from database import Database
from mod_events.controllers import mod_events

app = Flask(__name__)
app.register_blueprint(mod_events)
app.secret_key = os.urandom(24)

Database.create_db('/home/lama/Code/Python/python-flask-events-codecool/database.sql')


@app.route("/")
def index():
    """ Redirects to list of events stored in the database.
    """
    return redirect(url_for('mod_events.index'))


if __name__ == "__main__":
    app.run()
