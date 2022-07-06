from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')

@app.route("/test")
def make_rec():
    return jsonify(message='Invoked test endpoint!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
