from website import db
from flask_login import UserMixin
from datetime import datetime

class JobSeeker(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    profile_pic = db.Column(db.String(150))
    gender = db.Column(db.String(20), nullable=False)
    linkedin_page = db.Column(db.String(150))
    nationality = db.Column(db.String(100), nullable=False)
    current_job_position = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(150), nullable=False)
    experience = db.Column(db.String(150), nullable=False)
    resume = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
 
class AppliedJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    jobseeker_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    middle_name = db.Column(db.String(150), nullable=True)
    last_name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    cover_letter = db.Column(db.Text, nullable=False)
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

    job = db.relationship('Job', backref=db.backref('applied_jobs', lazy=True))
    job_seeker = db.relationship('JobSeeker', backref=db.backref('applied_jobs', lazy=True))