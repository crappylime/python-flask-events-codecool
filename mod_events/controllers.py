from flask import Blueprint
from mod_events.models import Event

mod_events = Blueprint('mod_events', __name__)


@mod_events.route("/")
def index():
    """ Shows list of events stored in the database.
    """
    return 'Hello'
