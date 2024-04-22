#!/usr/bin/python3
"""
    dynamic cities_by_states module
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ terminates connection between the app and the database """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
        defining cities by states route
        accesses the data from storage backend
    """
    states = storage.all(State).values()
    for key in states:
        if not hasattr(key, 'cities'):
            setattr(key, 'cities', key.cities)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
