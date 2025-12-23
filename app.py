# app.py
from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/health")
def health():
    logging.info("Health endpoint called")
    return jsonify({"status": "OK"})

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(port=5000)
