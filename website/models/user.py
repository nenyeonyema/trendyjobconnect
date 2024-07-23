from .. import db
from flask_login import UserMixin
from datetime import datetime

class JobSeeker(UserMixin, db.Model):
    __tablename__ = 'jobseeker'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_pic = db.Column(db.String(100), nullable=False)
    current_position = db.Column(db.String(100), nullable=False)
    is_employer = db.Column(db.Boolean, default=False)
    applied_jobs = db.relationship('AppliedJob', backref='job_seeker', lazy=True)

    def __init__(self, email, password, first_name, last_name, profile_pic=None, current_position=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.profile_pic = profile_pic
        self.current_position = current_position

class Employer(UserMixin, db.Model):
    __tablename__ = 'employer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    company_location = db.Column(db.String(100), nullable=False)
    company_logo = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_employer = db.Column(db.Boolean, default=True)
    jobs = db.relationship('Job', backref='employer', lazy=True)

    def __init__(self, email, password, company_name, company_logo=None, company_website=None):
        self.email = email
        self.password = password
        self.company_name = company_name
        self.company_logo = company_logo
        self.company_website = company_website

class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    responsibilities = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    expires_on = db.Column(db.DateTime, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)

    def __init__(self, title, company_name, description, requirements, responsibilities, location, type, expires_on, industry, benefits, user_id):
        self.title = title
        self.company_name = company_name
        self.description = description
        self.requirements = requirements
        self.responsibilities = responsibilities
        self.location = location
        self.type = type
        self.expires_on = expires_on
        self.industry = industry
        self.benefits = benefits
        self.user_id = user_id

class AppliedJob(db.Model):
    __tablename__ = 'appliedjob'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    cover_letter = db.Column(db.Text, nullable=False)
    resume = db.Column(db.Text, nullable=False)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('jobseeker.id'), nullable=False)

    def __init__(self, job_title, first_name, middle_name, last_name, email, phone_number, cover_letter, resume, job_id, user_id):
        self.job_title = job_title
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.cover_letter = cover_letter
        self.resume = resume
        self.job_id = job_id
        self.user_id = user_id
