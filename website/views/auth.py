from flask import Blueprint, render_template, redirect, request, flash
from flask import Blueprint, render_template, redirect, url_for, flash
from ..validations.employer_validation import EmployerSignupForm
from ..validations.jobseeker_validation import JobSeekerSignupForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route("/login/jobseeker", methods=['POST'], strict_slashes=False)
def login_jobseeker():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        flash("Login successful", category='success')
        return redirect(url_for('dashboard_jobseeker'))

    return render_template('login.html', form=form)

@auth.route("/login/employer", methods=['POST'], strict_slashes=False)
def login_employer():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        flash("Login successful", category='success')
        return redirect(url_for('dashboard_employer'))

    return render_template('login_employer.html', form=form)


@auth.route("/logout/jobseeker", methods=['GET'], strict_slashes=False)
def logout_jobseeker():
    return redirect(url_for('login'))

@auth.route("/logout/employer", methods=['GET'], strict_slashes=False)
def logout_employer():
    return redirect(url_for('login_employer'))


@auth.route("/signup", methods=['GET'], strict_slashes=False)
def signup():
    return  render_template('signup_page.html')

@auth.route("/signup/jobseeker", methods=['POST'], strict_slashes=False)
def signup_jobseeker():
    form = JobSeekerSignupForm()
    if form.validate_on_submit():
        # Access form data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        nationality = form.nationality.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        current_job_position = form.current_job_position.data
        gender = form.gender.data
        profile_pic = form.profile_pic.data
        skills = form.skills.data
        experience = form.experience.data
        resume = form.resume.data

        flash("Sign up successful", category='success')
        return redirect(url_for('main.home'))

    return  render_template('signup_jobseeker.html')

@auth.route("/signup/employer", methods=['POST'], strict_slashes=False)
def signup_employer():
    form = EmployerSignupForm()
    if form.validate_on_submit():
        # Access form data
        company_name = form.company_name.data
        address = form.address.data
        zip_code = form.zip_code.data
        city = form.city.data
        country = form.country.data
        company_website = form.company_website.data
        industry = form.industry.data
        other_industry = form.other_industry.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        position = form.position.data
        email = form.email.data
        profile_pic = form.profile_pic.data
        gender = form.gender.data
        linkedin_page = form.linkedin_page.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        flash("Sign up successful", category='success')
        return redirect(url_for('main.home'))

    return  render_template('signup_employer.html')