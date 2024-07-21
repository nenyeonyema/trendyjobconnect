from ..models.user import db, Job, AppliedJob

def create_job(user_id, job_data):
    job = Job(
        title=job_data['title'],
        company_name=job_data['company_name'],
        responsibilities=job_data['responsibilities'],
        description=job_data['description'],
        requirements=job_data['requirements'],
        location=job_data['location'],
        expires_on=job_data['expires_on'],
        benefits=job_data['benefits'],
        type=job_data['type'],
        user_id=user_id
    )
    db.session.add(job)
    db.session.commit()
    return job

def apply_for_job(user_id, application_data):
    application = AppliedJob(
        job_title=application_data['job_title'],
        first_name=application_data['first_name'],
        middle_name=application_data['middle_name'],
        last_name=application_data['last_name'],
        email=application_data['email'],
        phone_number=application_data['phone_number'],
        cover_letter=application_data['cover_letter'],
        resume=application_data['resume'],
        job_id=application_data['job_id'],
        user_id=user_id
    )
    db.session.add(application)
    db.session.commit()
    return application

def apply_for_job(application_data):
    new_application = AppliedJob(**application_data)
    db.session.add(new_application)
    db.session.commit()

def get_job_by_id(job_id):
    return Job.query.get(job_id)
    
def get_all_jobs():
    return Job.query.all()
