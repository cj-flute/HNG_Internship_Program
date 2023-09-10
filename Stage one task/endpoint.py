from flask import Flask, request, jsonify
import datetime, time
import os
from dotenv import load_dotenv
load_dotenv()

endpoint = Flask(__name__)

@endpoint.route('/api', methods=['GET'])
def myAPI():
    q = request.args.to_dict()
    date_time_year = datetime.datetime.now()
    day = datetime.date(int(date_time_year.year),
        int(date_time_year.month), int(date_time_year.day)).strftime("%A")

    current_datetime = datetime.datetime.utcnow()
    formatted_date = current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
 
    # My API
    infoAPI = {
        "slack_name": q.get("slack_name"),
        "current_day": day,
        "utc_time": formatted_date,
        "track": q.get("track"),
        "github_file_url": 'https://github.com/cj-flute/repo/blob/main/endpoint.py',
        "github_repo_url": 'https://github.com/cj-flute/repo',
        "status_code": 200
    }
    return jsonify(infoAPI)


if __name__ == "__main__":
    endpoint.run()