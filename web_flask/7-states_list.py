#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def d_states():
    """displaying states"""
    return render_template('7-states_list.html', state_d=state_d)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
