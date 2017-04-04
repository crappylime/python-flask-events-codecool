from flask import Blueprint, render_template
from mod_events.models import Event

mod_events = Blueprint('mod_events', __name__)


@mod_events.route("/")
@mod_events.route("/events")
def index():
    """ Shows list of events stored in the database.
    """
    return render_template('index.html', events_list=Event.get_all())
