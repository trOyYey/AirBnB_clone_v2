#!/usr/bin/python3
"""
    100-hbnb path script
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """ terminates connection between the app and the database """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        main hbnb route
        accesses the data from storage backend
    """
    states = storage.all(State).values()
    for key in states:
        if not hasattr(key, 'cities'):
            setattr(state, 'cities', state.cities)
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    for key in places:
        owner = users[f"User.{key.user_id}"]
        setattr(key, "owner", f"{owner.first_name} {owner.last_name}")
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
