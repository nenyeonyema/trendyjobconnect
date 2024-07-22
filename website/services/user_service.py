from werkzeug.security import generate_password_hash
from ..models.user import db, Employer, JobSeeker


def create_jobseeker(data):
    existing_user = JobSeeker.query.filter_by(email=data['email']).first()
    if existing_user:
        raise ValueError("Email already registered")

    if data['password'] != data['confirm_password']:
        raise ValueError("Passwords do not match")

    password_hash = generate_password_hash(data['password'])
    jobseeker = JobSeeker(email=data['email'],
                          password=password_hash,
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
    password_hash = generate_password_hash(data['password'])
    employer = Employer(email=data['email'],
                        password=password_hash,
                        company_name=data['company_name'],
                        company_logo=data.get('company_logo'),
                        company_website=data.get('company_website'))
    db.session.add(employer)
    db.session.commit()
    return employer


def get_employer_by_id(user_id):
    return Employer.query.get(user_id)


def get_jobseeker_by_id(job_id):
    return JobSeeker.query.get(job_id)
