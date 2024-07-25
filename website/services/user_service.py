from werkzeug.security import generate_password_hash
from ..models.user import db, Employer, JobSeeker
from .. import bcrypt


def create_jobseeker(data):
    existing_user = JobSeeker.query.filter_by(email=data['email']).first()
    if existing_user:
        raise ValueError("Email already registered")

    if data['password'] != data['confirm_password']:
        raise ValueError("Passwords do not match")
    hashed_password = bcrypt.generate_password_hash(
        data['password']).decode('utf-8')
    # password_hash = generate_password_hash(data['password'])
    jobseeker = JobSeeker(email=data['email'],
                          password=hashed_password,
                          first_name=data['first_name'],
                          last_name=data['last_name'],
                          profile_pic=data['profile_pic'],
                          current_position=data['current_position'])

    db.session.add(jobseeker)
    db.session.commit()
    return jobseeker


def create_employer(data):
    existing_user = Employer.query.filter_by(email=data['email']).first()
    if existing_user:
        raise ValueError("Email already registered")

    if data['password'] != data['confirm_password']:
        raise ValueError("Passwords do not match")

    hashed_password = bcrypt.generate_password_hash(
        data['password']).decode('utf-8')

    employer = Employer(email=data['email'],
                        password=hashed_password,
                        company_location=data['company_location'],
                        company_name=data['company_name'],
                        company_logo=data['company_logo'],
                        company_website=data['company_website'])

    db.session.add(employer)
    db.session.commit()
    return employer


def get_employer_by_id(user_id):
    return Employer.query.get(user_id)


def get_jobseeker_by_id(job_id):
    return JobSeeker.query.get(job_id)
