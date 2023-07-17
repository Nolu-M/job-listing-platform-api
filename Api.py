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



@app.route('/job-search')
def job_search_route():

    try:
        job_instance = db('jobs')

        tmp_jobListings = []

        rows = job_instance.select()

        for row in rows:
            tmp_job = {
                "id": row[0],
                "job_name": row[1],
                "job_type": row[2],
                "job_posted": row[3],
                "job_location": row[4],
            }

            tmp_jobListings.append(tmp_job)

        jobListings_dict = {
            "jobs": tmp_jobListings
        }

    except AttributeError:
        print('No such attribute')
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