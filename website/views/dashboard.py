from flask import Blueprint, render_template, redirect, url_for, flash, request
from validations.posted_job import PostJobForm
from models.employer import Job
from website import db
from flask_login import login_required, current_user

dashboard = Blueprint('job', __name__)

@dashboard.route("/employer", methods=['GET'], strict_slashes=False)
@login_required
def employer_dashboard():
    return render_template('dashboard_employer.html', user=current_user)

@dashboard.route("/employer", methods=['GET'], strict_slashes=False)
@login_required
def employer_dashboard():
    return render_template('dashboard_jobseeker.html', user=current_user)