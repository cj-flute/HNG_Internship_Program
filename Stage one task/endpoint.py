from flask import Flask, request, jsonify
import datetime, time

endpoint = Flask(__name__)

@endpoint.route('/api', methods=['GET'])
def myAPI():
    q = request.args.to_dict()


    # For the date and time (auto-generated)
    dt = datetime.date.today()
    t = time.strftime("%H:%M:%S")
    dtt = f"{dt}T{t}Z"
    date_time_year = datetime.datetime.now()
    day = datetime.date(int(date_time_year.year),
        int(date_time_year.month), int(date_time_year.day)).strftime("%A")
 
    # My API
    infoAPI = {
        "slack_name": q.get("slack_name"),
        "current_day": day,
        "utc_time": dtt,
        "track": q.get("track"),
        "github_file_url": 'https://github.com/cj-flute/repo/blob/main/endpoint.py',
        "github_repo_url": 'https://github.com/cj-flute/repo',
        "status_code": 200
    }
    return jsonify(infoAPI)


if __name__ == "__main__":
    endpoint.run(port=4000, debug=True)