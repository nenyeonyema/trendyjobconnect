from flask import Blueprint, render_template, current_app
from ..services.apicalls import  fetch_jobs

homepage = Blueprint('homepage', __name__)


@homepage.route('/', methods=['GET'])
def home():
    jobs = fetch_jobs(current_app)
    return render_template('home.html', jobs=jobs)
