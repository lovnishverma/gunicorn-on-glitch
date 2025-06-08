from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import os

app = Flask(__name__)

@app.route('/')
def test():
    return render_template("index.html")

@app.route('/time')
def get_current_time():
    now = datetime.utcnow()
    return jsonify({"current_utc_time": now.isoformat() + 'Z'})

@app.route('/add_days', methods=['POST'])
def add_days():
    data = request.get_json(force=True, silent=True)
    if not data or 'days' not in data:
        return jsonify({"error": "Missing 'days' parameter"}), 400
    try:
        days = int(data['days'])
    except ValueError:
        return jsonify({"error": "'days' must be an integer"}), 400

    future_date = datetime.utcnow() + timedelta(days=days)
    return jsonify({"future_date": future_date.isoformat() + 'Z', "days_added": days})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
