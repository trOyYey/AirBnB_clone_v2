#!/usr/bin/python3
"""
    home route model
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """defining home route """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
