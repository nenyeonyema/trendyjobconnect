from werkzeug.security import generate_password_hash
from models.user import db, User

def create_employer(data):
    password_hash = generate_password_hash(data['password'])
    employer = User(
        email=data['email'],
        password=password_hash,
        is_employer=True,
        company_name=data['company_name'],
        # Add other employer-specific fields here
    )
    db.session.add(employer)
    db.session.commit()
    return employer

def create_jobseeker(data):
    password_hash = generate_password_hash(data['password'])
    jobseeker = User(
        email=data['email'],
        password=password_hash,
        is_employer=False,
        first_name=data['first_name'],
        last_name=data['last_name'],
    )
    db.session.add(jobseeker)
    db.session.commit()
    return jobseeker
