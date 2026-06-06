from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("NEWSDATA_API_KEY")

@app.route("/news")
def news():
    category = request.args.get("category", "technology")
    language = request.args.get("language", "en")

    response = requests.get(
        "https://newsdata.io/api/1/news",
        params={
            "apikey": API_KEY,
            "language": language,
            "category": category
        },
        timeout=30
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
