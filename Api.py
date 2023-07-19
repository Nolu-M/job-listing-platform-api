from flask import Flask, request
from flask_cors import CORS

import config

from db import db


app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Careers API"


@app.route('/create_job_alert', methods=["POST"])
def create_job_alert_route():
    data = request.form
    
    job = data['job']
    province = data['province']
    city = data['city']
    email = data['email']

    try:
        email_alert_instance = db('email_alert')

        email_alert_rows = email_alert_instance.select(condition=f"WHERE email='{email}'")
        email_alert_id = None

        if len(email_alert_rows):
            email_alert_id = email_alert_rows[0][0]
        else:
            email_alert_id = email_alert_instance.insert("job, province, city, email", f"'{job}', '{province}', '{city}', '{email}'")

    except AttributeError:
        print('No such attribute')  
    return f'Submission from {job} {province} {city} {email}'
  


@app.route('/submit', methods=['POST'])
def submit_job_listing():
    
    title = request.form['title']
    company = request.form['company']
    location = request.form['location']
    salary = request.form['salary']
    description = request.form['description']
    requirements = request.form['requirements']

    return 'Job listing successfully submitted'
 

@app.route('/job-search')
def job_search_route():

        tmp_jobListings = [
            {
                "title": "Software engineer",
                "type": "Job-type: Permanent",
                "posted": "Posted: 27 June 2023",
                "location": "Location: Eastern Cape",
                "path": "/job-search/software-engineer"
            },
            {
                "title": "Backend engineer",
                "type": "Job-type: Contract",
                "posted": "Posted: 29 June 2023",
                "location": "Location: Eastern Cape",
                "path": "/job-search/backend-engineer"
            },
            {
                "title": "Frontend engineer",
                "type": "Job-type: Permanent",
                "posted": "Posted: 22 June 2023",
                "location": "Location: Western Cape",
                "path": "/job-search/frontend-engineer"
            }
        ]


        jobListings_dict = {
            "jobs": tmp_jobListings
        }

        return jobListings_dict



@app.route('/job-search/<job_slug>')
def job_route(job_slug):

    try:
        job_instance = db('job')

        rows = job_instance.select(condition=f"WHERE slug='{job_slug}'")

        if len(rows):
            row = rows[0]

            tmp_job = {
                "id": row[0],
                "job_title": row[1],
                "company": row[2],
                "job_location": row[3],
                "job_desc": row[4],
                "job_req_": row[5]
            }
    except AttributeError:
        print('No such attribute')
        return tmp_job
    else:
        return {}
