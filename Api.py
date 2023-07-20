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

    email_alert_instance = db('email_alert')

    email_alert_rows = email_alert_instance.select(condition=f"WHERE email='{email}'")
    email_alert_id = None

    if len(email_alert_rows):
        email_alert_id = email_alert_rows[0][0]
    else:
        email_alert_id = email_alert_instance.insert("job, province, city, email", f"'{job}', '{province}', '{city}', '{email}'")
  
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
        tmp_jobs = []

        jobs_instance = db('jobs')

        rows = jobs_instance.select()

        for row in rows:
            tmp_job = {
                "id": row[0],
                "job_title": row[1],
                "job_type": row[2],
                "job_posted": row[3],
                "job_location": row[4],
                "job_slug": row[5]
            }

            tmp_jobs.append(tmp_job)

        jobs_dict = {
            "jobs": tmp_jobs
        }

        return jobs_dict



@app.route('/job-search/<job_slug>')
def job_route(job_slug):
        tmp_jobs = []

        job_instance = db('job')

        rows = job_instance.select(condition=f"WHERE slug='{job_slug}'")

        for row in rows:
            tmp_job = {
                "id": row[0],
                "title": row[1],
                "company": row[2],
                "job_location": row[3],
                "salary": row[4],
                "description": row[5],
                "requirements": row[6],
                "slug": row[7]
            }

            tmp_jobs.append(tmp_job)

        job_dict = {
            "job": tmp_job
        }

        return job_dict
