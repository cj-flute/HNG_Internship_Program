from flask import Flask, request, jsonify

endpoint = Flask(__name__)

@endpoint.route('/endpoint', methods=['GET'])
def myAPI():
    git_file_url = request.args.get('https://github.com/cj-flute/repo/blob/main/endpoint.py')
    git_repo_url = request.args.get('https://github.com/cj-flute/repo')
    infoAPI = {
        "slack_name": "CjFlute",
        "current_day": "Friday",
        "utc_time": "2023-09-08T12:09:05Z",
        "track": "backend",
        "github_file_url": git_file_url,
        "github_repo_url": git_repo_url,
        "status_code": 200,
    }
    return jsonify(infoAPI)
    pass

if __name__ == "__main__":
    endpoint.run(debug=True)