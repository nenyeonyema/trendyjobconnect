from models.jobseeker import JobSeeker, AppliedJob
from werkzeug.security import generate_password_hash

def create_jobseeker(data):
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_employer = JobSeeker(
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

def create_appliedjob(data):
    new_application = AppliedJob(
        firstname=data['first-name'],
        middlename=data['middle-name'],
        lastname=data['last-name'],
        email=data['email'],
        phonenumber=data['phone-number'],
        position=data['position'],
        cover_letter=data['cover-letter'],
        resume=data.get('resume')
    )
    new_application.save()  # Save the employer to the database

    return new_application
