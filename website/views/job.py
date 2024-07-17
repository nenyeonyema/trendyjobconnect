from flask import Blueprint, render_template, request, redirect, url_for, flash
from validations.employer_validation import JobPostForm
from validations.jobseeker_validation import AppliedJobForm
from services.employer import create_job
from services.jobseeker import create_appliedjob
from flask_login import login_required, current_user

job = Blueprint('job', __name__)


@job.route('/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    form = JobPostForm()
    if form.validate_on_submit():
        job_data = {
            'job_title': form.job_title.data,
            'company_name': form.company_name.data,
            'job_description': form.job_description.data,
            'responsibilities': form.responsibilities.data,
            'requirements': form.requirements.data,
            'job_location': form.job_location.data,
            'job_type': form.job_type.data,
            'expires_on': form.expires_on.data,
            'benefits': form.benefits.data,
            'contact_first_name': form.contact_first_name.data,
            'contact_last_name': form.contact_last_name.data,
            'contact_email': form.contact_email.data,
            'job_position': form.job_position.data,
            'corporate_logo': form.corporate_logo.data
        }
        try:
            job = create_job(current_user.id, job_data)
            flash('Job posted successfully!', 'success')
            return redirect(url_for('dashboard.employer', job_id=job.id))
        except Exception as e:
            flash(f'Error creating account: {e}', 'danger')
    return render_template('post_job.html', form=form)


@job.route('/apply/<int:job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def apply_job(job_id):
    form = AppliedJobForm()
    if form.validate_on_submit():
        job_data = {
            'job_id': job_id,
            'jobseeker_id': current_user.id,
            'first_name': form.first_name.data,
            'middle_name': form.middle_name.data,
            'last_name': form.last_name.data,
            'phone_number': form.phone_number.data,
            'position': form.position.data,
            'email': form.email.data,
            'cover_letter': form.cover_letter.data
        }
        try:
            create_appliedjob(job_data)
            flash('Your application has been submitted.', 'success')
            return redirect(url_for('dashboard.jobseeker'))
        except Exception as e:
            flash(f'Error creating account: {e}', 'danger')
    return render_template('job_form.html', form=form)
