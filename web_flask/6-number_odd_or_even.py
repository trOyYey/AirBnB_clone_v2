#!/usr/bin/python3
"""
    /C route model
"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_template_only_numbers(n):
    """
    defining number_template route which takes
    url arguments only if they presented as int
    and then renders a template
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_numbers(n):
    """
    defining number_template route which
    takes url arguments only if they present as
    int and renders a template from that number
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
