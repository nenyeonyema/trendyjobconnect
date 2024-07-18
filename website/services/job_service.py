from ..models.user import db, Job, AppliedJob

def create_job(user_id, job_data):
    job = Job(
        title=job_data['title'],
        description=job_data['description'],
        requirements=job_data['requirements'],
        location=job_data['location'],
        type=job_data['type'],
        user_id=user_id
    )
    db.session.add(job)
    db.session.commit()
    return job

def apply_for_job(user_id, application_data):
    application = AppliedJob(
        first_name=application_data['first_name'],
        last_name=application_data['last_name'],
        email=application_data['email'],
        phone_number=application_data['phone_number'],
        cover_letter=application_data['cover_letter'],
        job_id=application_data['job_id'],
        user_id=user_id
    )
    db.session.add(application)
    db.session.commit()
    return application

def get_all_jobs():
    return Job.query.all()
