from flask import Flask, request, jsonify

endpoint = Flask(__name__)

@end_point.route('/endpoint', methods=['GET'])
def myAPI():
    infoAPI = {
        "slack_name": "CjFlute",
        "current_day": "Friday",
        "utc_time": "2023-09-08T12:09:05Z",
        "track": "backend",
        "github_file_url": "https://github.com/cj-flute/repo/blob/main"
    }
    return api
    pass

if __name__ == "__main__":
    endpoint.run(debug=True)