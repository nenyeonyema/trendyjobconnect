import os
import requests


def search_jobs(query, location, distance='1.0', language='en_GB', remote_only='false', date_posted='month', employment_types='fulltime;parttime;intern;contractor', index='0'):
    api_url = 'https://jobs-api14.p.rapidapi.com/list'
    headers = {
        'x-rapidapi-host': RAPIDAPI_HOST,
        'x-rapidapi-key': RAPIDAPI_KEY
    }

    params = {
        'query': query,
        'location': location,
        'distance': distance,
        'language': language,
        'remoteOnly': remote_only,
        'datePosted': date_posted,
        'employmentTypes': employment_types,
        'index': index
    }

    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        job_list = response.json()
        return job_list
    else:
        print(f"Failed to retrieve jobs: {response.status_code}")
        return []


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
    if response.status_code == 200:
        response = requests.get(api_url, params=params)
    
        for job in response['jobs']:
            location = job.get('location', {})
            location_parts = location.get('area', [])
            formatted_location = ' > '.join(location_parts) if location_parts else location.get('display_name', 'Location not specified')
    
            jobs.append({
                'title': job['title'],
                'company': job['company']['display_name'] if 'company' in job else 'Unknown Company',
                'location': formatted_location,
                'job_type': job.get('contract_time', 'Not specified'),
                'salary': f"{job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}",
                'url': job['redirect_url']
            })
    
        return jobs
    else:
        return []

def job_board():
    api_url = 'https://jobs-api14.p.rapidapi.com/list'
    headers = {
        'x-rapidapi-host': RAPIDAPI_HOST,
        'x-rapidapi-key': RAPIDAPI_KEY
    }
    params = {
        'query': 'Web Developer',
        'location': 'United States',
        'distance': '1.0',
        'language': 'en_GB',
        'remoteOnly': 'false',
        'datePosted': 'month',
        'employmentTypes': 'fulltime;parttime;intern;contractor',
        'index': '0'
    }

    response = requests.get(apiurl, headers=headers, params=params)

    if response.status_code == 200:
        job_list = response.json()
        return job_list
    else:
        print(f"Failed to retrieve jobs: {response.status_code}")
        return []

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
