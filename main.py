from flask import Flask
from mod_events.controllers import mod_events
from database import Database

app = Flask(__name__)
app.register_blueprint(mod_events)

Database.create_db('database.sql')

if __name__ == "__main__":
    app.run()
