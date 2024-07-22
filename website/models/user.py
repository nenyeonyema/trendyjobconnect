from .. import db
from flask_login import UserMixin
from datetime import datetime


class JobSeeker(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profile_pic = db.Column(db.String(100), nullable=False)
    current_position = db.Column(db.String(100), nullable=False)
    is_employer = db.Column(db.Boolean, default=False)
    applied_jobs = db.relationship('AppliedJob',
                                   backref='job_seeker',
                                   lazy=True)


class Employer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    company_location = db.Column(db.String(100), nullable=False)
    company_logo = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_employer = db.Column(db.Boolean, default=True)
    jobs = db.relationship('Job', backref='employer', lazy=True)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    responsibilties = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('employer.id'),
                        nullable=False)


class AppliedJob(db.Model):
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
    user_id = db.Column(db.Integer,
                        db.ForeignKey('jobseeker.id'),
                        nullable=False)

    job = db.relationship('Job', backref=db.backref('applications', lazy=True))
    user = db.relationship('User',
                           backref=db.backref('applications', lazy=True))
