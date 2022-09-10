#!/usr/bin/python3
"""script that starts a Flask web application"""
from pydoc import render_doc
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """should display the string “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hello_world2():
    """should display the string “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """should display the string"C "followed by
    the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """should display the string "Python " followed by
    the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return str(n) + ' is a number'


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    roulette = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, roulette=roulette)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
