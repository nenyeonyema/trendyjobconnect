from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms import EmailField, IntegerField, TextAreaField, SelectField, URLField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed


class EmployerSignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    company_location = StringField('Company Location',
                                   validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    company_logo = FileField(
        'Company Logo',
        validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    company_website = URLField('Company Website', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class JobSeekerSignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(),
                                        EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    current_position = StringField('Current Position',
                                   validators=[DataRequired()])
    profile_pic = FileField('Profile Picture')
    submit = SubmitField('Sign Up')


class AppliedJobForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    cover_letter = TextAreaField('Cover Letter', validators=[DataRequired()])
    resume = FileField(
        'Resume',
        validators=[FileAllowed(['pdf', 'doc', 'docx'], 'Documents only!')])
    submit = SubmitField('Apply')

    def validate_first_name(self, first_name):
        if not first_name.data.strip():
            raise ValidationError(
                'First name cannot be empty or only whitespace.')

    def validate_middle_name(self, middle_name):
        if not middle_name.data.strip():
            raise ValidationError(
                'Middle name cannot be empty or only whitespace.')

    def validate_last_name(self, last_name):
        if not last_name.data.strip():
            raise ValidationError(
                'Last name cannot be empty or only whitespace.')

    def validate_email(self, email):
        if not '@' in email.data or not '.' in email.data.split('@')[-1]:
            raise ValidationError('Invalid email address.')

    def validate_phone_number(self, phone_number):
        if not phone_number.data.strip():
            raise ValidationError(
                'Phone number cannot be empty or only whitespace.')

    def validate_cover_letter(self, cover_letter):
        if len(cover_letter.data) < 10:
            raise ValidationError(
                'Cover letter must be at least 10 characters long.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class JobPostForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    description = TextAreaField('Job Description', validators=[DataRequired()])
    responsibilities = TextAreaField('Responsibilities',
                                     validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    industry = StringField('Job Industry', validators=[DataRequired()])
    expires_on = DateField('Job Expiration',
                           format='%Y-%m-%d',
                           validators=[DataRequired()])
    location = StringField('Job Location', validators=[DataRequired()])
    job_type = SelectField('Job Type',
                           choices=[('full-time', 'Full Time'),
                                    ('part-time', 'Part Time')],
                           validators=[DataRequired()])
    benefits = TextAreaField('Benefits')

    def validate_title(self, title):
        if not title.data.strip():
            raise ValidationError(
                'Job title cannot be empty or only whitespace.')
        # if not title.data.isalpha():
        #     raise ValidationError('Job title must contain only alphabetic characters.')

    def validate_company_name(self, company_name):
        if not company_name.data.strip():
            raise ValidationError(
                'Company name cannot be empty or only whitespace.')
        # if not company_name.data.isalpha():
        #     raise ValidationError('Company name must contain only alphabetic characters.')

    def validate_email(self, email):
        # Custom email domain validation example
        # if '@example.com' not in email.data:
        #     raise ValidationError('Email must be a valid example.com address.')
        if not '@' in email.data or not '.' in email.data.split('@')[-1]:
            raise ValidationError('Invalid email address.')

    def validate_description(self, description):
        if len(description.data) < 10:
            raise ValidationError(
                'Job description must be at least 10 characters long.')

    def validate_requirements(self, requirements):
        if len(requirements.data) < 10:
            raise ValidationError(
                'Job requirements must be at least 10 characters long.')

    def validate_responsibilities(self, responsibilities):
        if len(responsibilities.data) < 10:
            raise ValidationError(
                'Job responsibilities must be at least 10 characters long.')

    def validate_location(self, location):
        if not location.data.strip():
            raise ValidationError(
                'Job location cannot be empty or only whitespace.')
        # if not location.data.isalpha():
        #     raise ValidationError('Job location must contain only alphabetic characters.')

    # def validate_job_type(self, job_type):
    #     if job_type.data not in ['Full Time', 'Part Time', 'Contract']:
    #         raise ValidationError('Invalid job type selected.')

    def validate_industry(self, industry):
        if not industry.data.strip():
            raise ValidationError(
                'Industry cannot be empty or only whitespace.')
        # if not industry.data.isalpha():
        #     raise ValidationError('Industry must contain only alphabetic characters.')

    def validate_benefits(self, benefits):
        if benefits.data and len(benefits.data) < 5:
            raise ValidationError(
                'Job benefits must be at least 5 characters long if provided.')


class JobSearchForm(FlaskForm):
    industry = StringField('Industry', validators=[DataRequired()])
    submit = SubmitField('Search')
