from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms import StringField, EmailField, IntegerField, TextAreaField, FileField, SelectField 
from wtforms.validators import DataRequired, Email, EqualTo 

class EmployerSignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    company_name = StringField('Company Name', validators=[DataRequired()])
    company_logo = FileField('Company Logo')
    company_website = StringField('LinkedIn Page', validators=[DataRequired(), URL()])
    submit = SubmitField('Sign Up')

class JobSeekerSignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    current_position = StringField('Company Name', validators=[DataRequired()])
    profile_pic = FileField('Profile Picture')
    submit = SubmitField('Sign Up')

class AppliedJobForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    cover_letter = TextAreaField('Cover Letter', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    submit = SubmitField('Apply')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class JobPostForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    responsibilities = TextAreaField('Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    job_location = StringField('Job Location', validators=[DataRequired()])
    job_type = SelectField('Job Type', choices=[('full-time', 'Full Time'), ('part-time', 'Part Time')], validators=[DataRequired()])
    expires_on = DateField('Job Expiration', format='%Y-%m-%d', validators=[DataRequired()])
    benefits = TextAreaField('Benefits')
    