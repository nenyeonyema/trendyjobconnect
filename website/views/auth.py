from flask import Blueprint, render_template, redirect, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['POST'], strict_slashes=False)
def login():
    # data = request.form
    # print(data)
    email = request.form.get('email')
    password = request.form.get('password')

    return render_template('login.html')

@auth.route("/logout")
def logout():
    return redirect(url_for('home'))

@auth.route("/signup", methods=['GET'], strict_slashes=False)
def signup():
    return  render_template('signup_page.html')

@auth.route("/signup/jobseeker", methods=['POST'], strict_slashes=False)
def signup_jobseeker():
    firstname = request.form.get('first-name')
    lastname = request.form.get('last-name')
    email = request.form.get('email')
    nationality = request.form.get('nationality')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    current_job_position = request.form.get('current-job-position')
    gender = request.form.get('gender')
    profile_pic = request.form.get('profile-pic')
    skills = request.form.get('skills')
    experience = request.form.get('experience')
    resume = request.form,get('resume')

    # if not firstname || not lastname || not email:
        # flash("Details in c", category='error')
        # flash("Details in complete", category='success')
    # else:
    #     flash("Sign up successful", category='success')
    #     return redirect(url_for('home'))

    return  render_template('signup_jobseeker.html')

@auth.route("/signup/employer", methods=['POST'], strict_slashes=False)
def signup_employer():
    company_name = request.form.get('company-name')
    address = request.form.get('address')
    zip_code = request.form.get('zip-code')
    city = request.form.get('city')
    country = request.form.get('country')
    company_website = request.form.get('company-website')
    industry = request.form.get('industry')
    other_industry = request.form.get('other_industry')
    firstname = request.form.get('first-name')
    lastname = request.form.get('last-name')
    position = request.form.get('position')
    email = request.form.get('email')
    profile_pic = request.form.get('profile-pic')
    gender = request.form.get('gender')
    linkedin_page = request.form.get('linkedin-page')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    
    return  render_template('signup_employer.html')