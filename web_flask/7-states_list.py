#!/usr/bin/python3
"""
    dynamic state list module
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ terminates connection between the app and the database """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
        defining states list route
        accesses the data from storage backend
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
