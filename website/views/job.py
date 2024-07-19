from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..models.user import Job, AppliedJob
from ..services.job_service import create_job, apply_for_job
from ..validation.forms import AppliedJobForm, JobPostForm, JobSearchForm
from ..services.job_service import get_all_jobs

job = Blueprint('job', __name__)

@job.route('/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if not current_user.is_employer:
        flash('Only employers can post jobs.', 'danger')
        return redirect(url_for('auth.login'))
    form = JobPostForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            job_data = {
                'company_name': request.form['company-name'],
                'title': request.form['job-title'],
                'description': request.form['job-description'],
                'responsibilities': request.form['responsibilities'],
                'requirements': request.form['requirements'],
                'location': request.form['job-location'],
                'expires_on': request.form['expires-on'],
                'type': request.form['job-type'],
                'benefits': request.form['benefits'],
                'user_id': current_user.id
            }

        job = create_job(current_user.id, job_data)
        flash('Job posted successfully!', 'success')
        return redirect(url_for('job.dashboard_employer'))
    return render_template('post_job.html')

@job.route('/jobs', methods=['GET'])
@login_required
def list_jobs():
    jobs = get_all_jobs()
    return render_template('list_jobs.html', jobs=jobs)

@job.route('/job/<int:job_id>', methods=['GET'])
@login_required
def job_details(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)

@job.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply_job(job_id):
    form = AppliedJobForm()
    if form.validate_on_submit():
        application_data = {
            'first_name': request.form['first-name'],
            'middle_name': request.form['middle-name'],
            'last_name': request.form['last-name'],
            'email': request.form['email'],
            'phone_number': request.form['phone-number'],
            'job_title': request.form['job-title'],
            'cover_letter': request.form['cover-letter'],
            'job_id': job_id,
            'user_id': current_user.id
        }
        apply_for_job(application_data)
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('job.list_jobs'))
    return render_template('apply_job.html', form=form, job_id=job_id)

@job.route('/dashboard/employer', methods=['GET'])
@login_required
def dashboard_employer():
    if not current_user.is_employer:
        flash('Access denied.', 'danger')
        return redirect(url_for('auth.login'))
    jobs = Job.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard_employer.html', jobs=jobs, companyname=current_user.company_name, companylocation=current_user.company_location, companylogo=current_user.company_logo, email=current_user.email)

@job.route('/dashboard/jobseeker', methods=['GET'])
@login_required
def dashboard_jobseeker():
    if current_user.is_employer:
        flash('Access denied.', 'danger')
        return redirect(url_for('auth.login'))
    applied_jobs = AppliedJob.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard_jobseeker.html', applied_jobs=applied_jobs, firstname=current_user.first_name, lastname=current_user.first_name, profilepic=current_user.profile_pic, current_position=current_user.current_position, email=current_user.email)


@job.route('/search', methods=['GET', 'POST'])
def search_jobs():
    form = JobSearchForm()
    jobs = []
    if form.validate_on_submit():
        industry = request.form['industry']
        jobs = Job.query.filter_by(industry=industry).all()
    return render_template('search_jobs.html', form=form, jobs=jobs)
