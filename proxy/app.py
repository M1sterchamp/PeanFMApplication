from flask import Flask, jsonify
import requests, os

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

@app.route("/version.json")
def version():
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.raw"
    }
    url = "https://api.github.com/repos/PeanFM/PeanFM-Desktop/contents/version.json"
    r = requests.get(url, headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
