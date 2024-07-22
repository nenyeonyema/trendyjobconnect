import requests


def search_jobs(query):
    api_url = "https://jobs-api14.p.rapidapi.com/list?query=Web%20Developer&location=United%20States&distance=1.0&language=en_GB&remoteOnly=false&datePosted=month&employmentTypes=fulltime%3Bparttime%3Bintern%3Bcontractor&index=0' \
	--header 'x-rapidapi-host: jobs-api14.p.rapidapi.com' \
	--header 'x-rapidapi-key: X-RAPIAPI-KEY'"

    params = {"query": query}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json().get("jobs", [])
    return []