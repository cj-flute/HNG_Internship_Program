from flask import Flask, request, jsonify
import datetime, time, requests

endpoint = Flask(__name__)

@endpoint.route('/endpoint', methods=['GET'])
def myAPI():
    # Parameters
    git_file_url = 'https://github.com/cj-flute/repo/blob/main/endpoint.py'
    git_repo_url = 'https://github.com/cj-flute/repo'
    response1 = requests.get(git_file_url)
    response2 = requests.get(git_repo_url)

    # slack_api_url = "https://slack.com/api/METHOD_FAMILY.method "
    # res = requests.get(slack_api_url)
    # userj = res.url

    # user
    # access_token = "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"
    # github_api_url = "https://api.github.com/user"
    # headers = {'Authorization': f'token {access_token}'} if access_token else {}
    # response = requests.get(github_api_url, headers=headers)
    # user_data = response.json()
    # username = user_data['login']

    # For the date and time (auto-generated)
    dt = datetime.date.today()
    t = time.strftime("%H:%M:%S")
    dtt = f"{dt}T{t}Z"
    date_time_year = datetime.datetime.now()
    day = datetime.date(int(date_time_year.year),
        int(date_time_year.month), int(date_time_year.day)).strftime("%A")

    # My API
    infoAPI = {
        "slack_name": "CjFlute",
        "current_day": day,
        "utc_time": dtt,
        "track": "Backend",
        "github_file_url": response1.url,
        "github_repo_url": response2.url,
        "status_code": response2.status_code,
    }
    return jsonify(infoAPI)
    pass

if __name__ == "__main__":
    endpoint.run(debug=True)