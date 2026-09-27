from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "tsetuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "testpass")

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello World"})

def get_db_conneciotn():
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn

@app.route("/dbtest")
def db_test():
    try:
        conn = get_db_conneciotn()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return jsonify({"db_connection": "successful"}), 200
        else:
            return jsonify({"db_connection": "failed"}), 500
    except Exception as e:
        return jsonify({"db_connection": "failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
