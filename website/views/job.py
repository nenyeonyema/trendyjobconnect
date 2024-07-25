from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from ..models.user import Job, AppliedJob
from ..services.job_service import create_job, apply_for_job, get_job_by_id, get_all_jobs
from ..services.apicalls import fetch_jobs, fetch_jobs_from_adzuna, fetch_jobs_from_joobleapi
from ..services.user_service import get_jobseeker_by_id, get_employer_by_id
from ..validation.forms import AppliedJobForm, JobPostForm, JobSearchForm

job = Blueprint('job', __name__)


@job.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if not current_user.is_employer:
        flash('Only employers can post jobs.', 'danger')
        return redirect(url_for('auth.login'))
    form = JobPostForm()

    if form.validate_on_submit():
        job_data = {
            'company_name': form.company_name.data,
            'title': form.job_title.data,
            'description': form.job_description.data,
            'responsibilities': form.responsibilities.data,
            'requirements': form.requirements.data,
            'location': form.job_location.data,
            'expires_on': form.expires_on.data,
            'industry': form.industry.data,
            'type': form.job_type.data,
            'benefits': form.benefits.data,
            'user_id': current_user.id
        }

        job = create_job(job_data)
        flash('Job posted successfully!', 'success')
        return redirect(url_for('job.dashboard_employer'))
    return render_template('post_job.html')


@job.route('/search_jobs', methods=['GET', 'POST'])
def search_jobs():

    search_query = request.form.get('search_query', '')

    adzuna_jobs = fetch_jobs_from_adzuna(current_app, search_query)

    print(adzuna_jobs)

    return render_template('list_jobs.html', jobs=adzuna_jobs)


# @job.route('/list_jobs', methods=['GET'])
# def list_jobs():
#     jobs = fetch_jobs(current_app)

#     if not jobs:
#         return flash('error No jobs found!'), 404
#     return render_template('list_jobs.html', jobs=jobs)
#     jobsdb = get_all_jobs()
#     return render_template('list_jobs.html', jobsdb=jobsdb, jobs=jobs)


@job.route('/job/<int:job_id>', methods=['GET'])
@login_required
def job_details(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)


@job.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply_job(job_id):
    job = get_job_by_id(job_id)
    if job is None:
        flash('Job not found.', 'danger')
        return redirect(url_for('job.list_jobs'))
    form = AppliedJobForm()
    if form.validate_on_submit():
        application_data = {
            'first_name': request.form['first-name'],
            'middle_name': request.form['middle-name'],
            'last_name': request.form['last-name'],
            'email': request.form['email'],
            'phone_number': request.form['phone-number'],
            'cover_letter': request.form['cover-letter'],
            'resume': request.form['resume'],
            'job_title': job.title,
            'job_id': job_id,
            'user_id': current_user.id
        }
        apply_for_job(application_data)
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('job.dashboard_jobseeker'))
    return render_template('apply_job.html', form=form, job=job, job_id=job_id)


@job.route('/dashboard/employer', methods=['GET'])
@login_required
def dashboard_employer():
    if not current_user.is_employer:
        flash('Access denied.', 'danger')
        return redirect(url_for('auth.login'))
    jobs = Job.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard_employer.html',
                           jobs=jobs,
                           companyname=current_user.company_name,
                           companylocation=current_user.company_location,
                           companylogo=current_user.company_logo,
                           email=current_user.email)


@job.route('/dashboard/jobseeker', methods=['GET'])
@login_required
def dashboard_jobseeker():
    if current_user.is_employer:
        flash('Access denied.', 'danger')
        return redirect(url_for('auth.login'))
    user = get_jobseeker_by_id(current_user.id)
    applied_jobs = AppliedJob.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard_jobseeker.html',
                           applied_jobs=applied_jobs,
                           email=current_user)


@job.route('/dashboard_search', methods=['GET', 'POST'])
@login_required
def search_job_db():
    # job_db = fetch_jobs_db()
    form = JobSearchForm()
    # jobs = []
    if form.validate_on_submit():
        industry = request.form['industry']
        jobs = Job.query.filter_by(industry=industry).all()
        return redirect(url_for('job.dashboard_employer'))
    return render_template('list_jobs.html')
