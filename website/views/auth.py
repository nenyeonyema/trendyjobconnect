from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app, session, send_from_directory
from flask_login import login_user, logout_user, login_required
from ..models.user import JobSeeker, Employer
from ..services.user_service import create_employer, create_jobseeker
from ..validation.forms import EmployerSignupForm, JobSeekerSignupForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import logging
from .. import bcrypt
# from ..services.user_service import get_employer, get_jobseeker
import imghdr
import uuid
import os

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']

        user1 = JobSeeker.query.filter_by(email=email).first()

        user2 = Employer.query.filter_by(email=email).first()

        user = user1 if user1 else user2

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            if isinstance(user, Employer):
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

        new_employer = {
            'email': form.email.data,
            'password': form.password.data,
            'confirm_password': form.confirm_password.data,
            'company_name': form.company_name.data,
            'company_logo': form.company_logo.data,
            'company_website': form.company_website.data,
            'industry': form.industry.data
        }
        try:
            create_employer(new_employer)
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'An error occurred while creating the account: {str(e)}',
                  'danger')

    return render_template('signup_employer.html', form=form)


@auth.route('/signup/jobseeker', methods=['GET', 'POST'])
def signup_jobseeker():
    form = JobSeekerSignupForm()
    if request.method == 'POST':
        logging.info("Form submission received")
        if form.validate_on_submit():
            logging.info("Form validated successfully")

            # upload_folder = 'path/to/save'

            profile_pic = request.files['profile_pic']
            if profile_pic:
                pic_filename = secure_filename(profile_pic.filename)
                filename = os.path.join(current_app.config['UPLOAD_PATH'],
                                        pic_filename)
                profile_pic.save(filename)

                profile_pic_url = f'uploads/{pic_filename}'
                # path_list = profile_pic.split('/')[1:]
                # profile_pic = '/'.join(path_list)
            else:
                profile_pic_url = 'profile_pic.jpg'

            new_jobseeker = {
                'email': form.email.data,
                'password': form.password.data,
                'confirm_password': form.confirm_password.data,
                'first_name': form.first_name.data,
                'last_name': form.last_name.data,
                'current_position': form.current_position.data,
                'profile_pic': profile_pic_url,
            }
            try:
                create_jobseeker(new_jobseeker)
                print('Account created successfully!', 'success')
                flash('Account created successfully!', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                print(f'Error creating account: {str(e)}', 'danger')
                flash(f'Error creating account: {str(e)}', 'danger')
    return render_template('signup_jobseeker.html', form=form)
