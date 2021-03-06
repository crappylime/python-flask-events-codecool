from flask import Blueprint, render_template, request, url_for, redirect, flash
from mod_events.models import Event

mod_events = Blueprint('mod_events', __name__,  url_prefix='/events')


@mod_events.route("/")
def index():
    """ Shows list of events stored in the database.
    """
    return render_template('index.html', events_list=Event.get_all())


@mod_events.route("/new")
def new():
    """ Shows new event form.
    """
    return render_template('form.html')


@mod_events.route("/create", methods=['POST'])
def create():
    """ Creates and saves new event.
    """
    if not request.form['name']:
        flash("Event's name is required")
    elif not request.form['date']:
        flash("Event's date is required")
    elif not request.form['description']:
        flash("Event's description is required")
    else:
        event = Event(name=request.form['name'], date=request.form['date'], description=request.form['description'])
        event.save()
        return redirect(url_for('mod_events.index'))
    return redirect(url_for('mod_events.new'))


@mod_events.route("/<int:id>/delete")
def delete(id):
    """ Removes event with selected id from the database """
    event = Event.get_by_id(id)
    event.delete()
    return redirect(url_for('mod_events.index'))


@mod_events.route("/<int:id>/edit", methods=['GET', 'POST'])
def edit(id):
    """ Edits event with selected id in the database
    If the method was GET it should show event form.
    If the method was POST it should update event in database.
    """
    event = Event.get_by_id(id)

    if request.method == 'POST':
        if not request.form['name']:
            flash("Event's name is required")
        elif not request.form['date']:
            flash("Event's date is required")
        elif not request.form['description']:
            flash("Event's description is required")
        else:
            event.name = request.form['name']
            event.date = request.form['date']
            event.description = request.form['description']
            event.save()
            return redirect(url_for('mod_events.index'))

    return render_template('form.html', event=event)
