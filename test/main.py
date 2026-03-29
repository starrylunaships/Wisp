from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

count = 0

@app.get("/addcount")
def index():
    global count
    count += 1
    return jsonify({"count": count}), 200

@app.get("/removecount")
def remove_count():
    global count
    count = 0
    return jsonify({"count": count}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
