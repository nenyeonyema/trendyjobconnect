import os
import requests
import urllib.parse
import json
from flask import current_app

def fetch_jobs_from_joobleapi(app, search_query, location):
    joobleapi_key = app.config['JOOBLE_API_KEY']

    api_url = "https://jooble.org/api/"
    headers = {
        "Content-type": "application/json"
    }
    body = json.dumps({
        "keywords": search_query,
        "location": location
    })

    response = requests.post(api_url + joobleapi_key, headers=headers, data=body)
    jobs = []

    if response.status_code == 200:
        job_data = response.json().get('jobs', [])
        for job in job_data:
            jobs.append({
                'title': job['title'],
                'location': job['location'],
                'job_type': job.get('type', 'Not specified'),
                'salary': job.get('salary', 'N/A'),
                'url': job['link']
            })

    return jobs


def fetch_jobs(app):
    adzuna_app_id = app.config['ADZUNA_APP_ID']
    adzuna_app_key = app.config['ADZUNA_APP_KEY']

    api_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        'app_id': adzuna_app_id,
        'app_key': adzuna_app_key,
        'results_per_page': 10,
        'content-type': 'application/json'
    }
    jobs = []

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        for job in data.get('results', []):
            location = job.get('location', {})
            location_parts = location.get('area', [])
            formatted_location = ' > '.join(
                location_parts) if location_parts else location.get(
                    'display_name', 'Location not specified')

            encoded_url = urllib.parse.quote(job.get('url', '#'))

            jobs.append({
                'title':
                job['title'],
                'company':
                job['company']['display_name']
                if 'company' in job else 'Unknown Company',
                'location':
                formatted_location,
                'job_type':
                job.get('contract_type', 'Not specified'),
                'salary':
                f"{job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}",
                'url':
                encoded_url,
                'description':
                job.get('description', 'No description available')
            })

        return jobs
    else:
        return []


def fetch_jobs_from_adzuna(app, search_query):
    adzuna_app_id = app.config['ADZUNA_APP_ID']
    adzuna_app_key = app.config['ADZUNA_APP_KEY']

    api_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        'app_id': adzuna_app_id,
        'app_key': adzuna_app_key,
        'results_per_page': 10,
        'content-type': 'application/json',
        'what': search_query
    }
    jobs = []

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        response_json = response.json()
        for job in response_json['results']:
            location = job.get('location', {})
            location_parts = location.get('area', [])
            formatted_location = ' > '.join(
                location_parts) if location_parts else location.get(
                    'display_name', 'Location not specified')

            encoded_url = urllib.parse.quote(job.get('redirect_url', '#'))

            jobs.append({
                'title':
                job['title'],
                'company':
                job['company']['display_name']
                if 'company' in job else 'Unknown Company',
                'location':
                formatted_location,
                'job_type':
                job.get('contract_type', 'Not specified'),
                'salary':
                f"{job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}",
                'url':
                encoded_url,
                'description':
                job.get('description', 'No description available')
            })

    return jobs


def list_jobs(app):
    adzuna_app_id = app.config['ADZUNA_APP_ID']
    adzuna_app_key = app.config['ADZUNA_APP_KEY']

    api_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        'app_id': adzuna_app_id,
        'app_key': adzuna_app_key,
        'results_per_page': 10,
        'content-type': 'application/json'
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
