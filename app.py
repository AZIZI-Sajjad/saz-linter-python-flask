from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello World"})

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000)
