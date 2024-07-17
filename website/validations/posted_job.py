from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, FileField, SubmitField
from wtforms.validators import DataRequired, Email

class PostJobForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    responsibilities = TextAreaField('Responsibilities', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    job_location = StringField('Job Location', validators=[DataRequired()])
    job_type = SelectField('Job Type', choices=[('full-time', 'Full Time'), ('part-time', 'Part Time')], validators=[DataRequired()])
    expires_on = DateField('Job Expiration', format='%Y-%m-%d', validators=[DataRequired()])
    benefits = TextAreaField('Benefits')
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    contact_email = StringField('Email', validators=[DataRequired(), Email()])
    job_position = StringField('Position', validators=[DataRequired()])
    corporate_logo = FileField('Upload Logo', validators=[])
    submit = SubmitField('Post Job')