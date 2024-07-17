from flask import Blueprint, render_template, redirect, url_for, flash
from validations.jobseeker_validation import JobSeekerSignupForm, LoginForm
from validations.employer_validation import EmployerSignupForm
from services.employer import create_employer

auth = Blueprint('auth', __name__)

@auth.route("/login/jobseeker", methods=['POST'], strict_slashes=False)
def login_jobseeker():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        flash("Login successful", category='success')
        return redirect(url_for('dashboard.jobseeker'))

    return render_template('login.html', form=form)

@auth.route("/login/employer", methods=['POST'], strict_slashes=False)
def login_employer():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        flash("Login successful", category='success')
        return redirect(url_for('dashboard.employer'))

    return render_template('login_employer.html', form=form)


@auth.route("/logout/jobseeker/<int id>", methods=['GET'], strict_slashes=False)
def logout_jobseeker():
    return redirect(url_for('login'))

@auth.route("/logout/employer/<int id>", methods=['GET'], strict_slashes=False)
def logout_employer():
    return redirect(url_for('login_employer'))


@auth.route("/signup", methods=['GET'], strict_slashes=False)
def signup():
    return  render_template('signup_page.html')

@auth.route("/signup/jobseeker", methods=['POST'], strict_slashes=False)
def signup_jobseeker():
    form = JobSeekerSignupForm()
    if form.validate_on_submit():
        data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'nationality': form.nationality.data,
            'password':form.password.data,
            'confirm_password': form.confirm_password.data,
            'current_job_position': form.current_job_position.data,
            'gender': form.gender.data,
            'profile_pic': form.profile_pic.data,
            'skills': form.skills.data,
            'experience': form.experience.data,
            'resume': form.resume.data,
        }

        try:
            jobseeker = create_employer(data)
            flash('Account created successfully!', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'Error creating account: {e}', 'danger')

    return  render_template('signup_jobseeker.html')

@auth.route('/signup/employer', methods=['GET', 'POST'])
def signup_employer():
    form = EmployerSignupForm()
    if form.validate_on_submit():
        data = {
            'company-name': form.company_name.data,
            'company-logo': form.company_logo.data,
            'address': form.address.data,
            'zip-code': form.zip_code.data,
            'city': form.city.data,
            'country': form.country.data,
            'company-website': form.company_website.data,
            'industry': form.industry.data,
            'other_industry': form.other_industry.data,
            'first-name': form.first_name.data,
            'last-name': form.last_name.data,
            'position': form.position.data,
            'email': form.email.data,
            'gender': form.gender.data,
            'linkedin-page': form.linkedin_page.data,
            'password': form.password.data,
            'confirm-password': form.confirm_password.data,
        }

        try:
            employer = create_employer(data)
            flash('Account created successfully!', 'success')
            return redirect(url_for('dashboard_employer'),
                            company_name=data['company-name'],
                            company_log=data.company_logo, )
        except Exception as e:
            flash(f'Error creating account: {e}', 'danger')

    return render_template('signup_employer.html', form=form)

