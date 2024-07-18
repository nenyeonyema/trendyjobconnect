from flask import Flask
from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route("/", methods=['GET'], strict_slashes=False)
def home():
    return render_template('home.html')