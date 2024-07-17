from website import db
from flask_login import UserMixin
# from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Employer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    zip_code = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    company_website = db.Column(db.String(150), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    other_industry = db.Column(db.Date, nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    profile_pic = db.Column(db.Text)
    linkedin_page =  db.Column(db.String(150))
    password= db.Column(db.String(150), nullable=False)
    password= db.Column(db.String(150), nullable=False)
    confirm_password= db.Column(db.String(150), nullable=False)
    corporate_logo = db.Column(db.String(150))


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(150), nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    responsibilities = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    job_location = db.Column(db.String(150), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    expires_on = db.Column(db.Date, nullable=False)
    benefits = db.Column(db.Text)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    job_position = db.Column(db.String(150), nullable=False)
    corporate_logo = db.Column(db.String(150))
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    employer = db.relationship('Employer', backref=db.backref('jobs', lazy=True))
    