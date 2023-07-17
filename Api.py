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

  