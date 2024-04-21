#!/usr/bin/python3
"""
    /C route model
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """defining home route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ defining hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """ C route that takes url path arguments """
    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text="is cool"):
    """ the python route that takes url path arguments """
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    defining number route which only
    takes url arguments if they are integer value
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
