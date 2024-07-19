from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models.user import User
from ..services.user_service import create_employer, create_jobseeker
from ..validation.forms import EmployerSignupForm, JobSeekerSignupForm, LoginForm
from werkzeug.security import check_password_hash
# from ..services.user_service import get_employer, get_jobseeker
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            if user.is_employer:
                return redirect(url_for('job.dashboard_employer'))
            else:
                return redirect(url_for('job.dashboard_jobseeker'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup_page():
    return render_template('signup_page.html')


@auth.route('/signup/employer', methods=['GET', 'POST'])
def signup_employer():
    form = EmployerSignupForm()
    if form.validate_on_submit():
        email = request.form['email']
        try:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email is already registered. Please log in.', 'danger')
            else:
                new_employer = {
                    'email': request.form['email'],
                    'password': request.form['password'],
                    'confirm_password': request.form['confirm-password'],
                    'company_name': request.form['comapny-name'],
                    'company_logo': request.form['company-logo'],
                    'company_website': request.form['company-website'],
                    'is_employer': request.form['is-employer'].lower() == 'true'
                }
                user = create_employer(new_employer)
                flash('Account created successfully!', 'success')
                return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'An error occurred while creating the account: {str(e)}', 'danger')

    return render_template('signup_employer.html', form=form)


@auth.route('/signup/jobseeker', methods=['GET', 'POST'])
def signup_jobseeker():
    form = JobSeekerSignupForm()
    if form.validate_on_submit():
        email = request.form['email']
        try:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash('Email is already registered. Please log in.', 'danger')
            else:
                new_jobseeker = {
                    'email': request.form['email'],
                    'password': request.form['password'],
                    'confirm_password': request.form['confirm-password'],
                    'first_name': request.form['first-name'],
                    'last-name': request.form['last-name'],
                    'profile_pic': request.form['profile-pic'],
                    'current_position': request.form['current-position']
                }
                user = create_jobseeker(new_jobseeker)
                flash('Account created successfully!', 'success')
                return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'An error occurred while creating the account: {str(e)}', 'danger')

    return render_template('signup_jobseeker.html', form=form)
