from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class JobSeekerSignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    current_job_position = StringField('Current Job Position', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    profile_pic = FileField('Profile Picture')
    skills = TextAreaField('Skills', validators=[DataRequired()])
    experience = TextAreaField('Experience', validators=[DataRequired()])
    resume = FileField('Resume', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AppliedJobForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cover_letter = StringField('Cover Letter', validators=[DataRequired(), Email()])

    