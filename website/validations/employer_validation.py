from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, DateField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class EmployerSignupForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    company_website = StringField('Company Website', validators=[DataRequired(), URL()])
    industry = StringField('Industry', validators=[DataRequired()])
    other_industry = StringField('Other Industry')
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_pic = FileField('Profile Picture')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    linkedin_page = StringField('LinkedIn Page', validators=[DataRequired(), URL()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


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
    contact_first_name = StringField('First Name', validators=[DataRequired()])
    contact_last_name = StringField('Last Name', validators=[DataRequired()])
    contact_email = StringField('Email', validators=[DataRequired(), Email()])
    job_position = StringField('Position', validators=[DataRequired()])
    corporate_logo = FileField('Upload Logo')
