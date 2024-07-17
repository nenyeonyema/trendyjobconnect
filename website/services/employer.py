from models.employer import Employer, Job
from website import db
from werkzeug.security import generate_password_hash
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_employer(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_employer = Employer(
        company_name=data['company-name'],
        address=data['address'],
        zip_code=data['zip-code'],
        city=data['city'],
        country=data['country'],
        company_website=data['company-website'],
        industry=data['industry'],
        other_industry=data.get('other_industry'),
        firstname=data['first-name'],
        lastname=data['last-name'],
        position=data['position'],
        email=data['email'],
        profile_pic=data.get('profile-pic'),
        gender=data['gender'],
        linkedin_page=data.get('linkedin-page'),
        password=hashed_password
    )
    new_employer.save()  # Save the employer to the database

    return new_employer

def create_job(employer_id, job_data):
    new_job = Job(**job_data, employer_id=employer_id)
    db.session.add(new_job)
    db.session.commit()
    return new_job

