#!/usr/bin/python3
"""
    dynamic state by city id module
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ terminates connection between the app and the database """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """
        defining states route
        accesses the data from storage backend
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_cities(id):
    """
        defining states cities route by id argument
        accesses the data from storage backend
    """
    state = storage.all(State).get(f"State.{id}")
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
