from flask import Flask
from flask_cors import CORS

import config

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Careers API"