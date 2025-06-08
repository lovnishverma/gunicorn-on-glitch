# server/relay_server.py
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
sessions = {}

@app.route('/register', methods=['POST'])
def register():
    code = request.json.get('code')
    ip = request.remote_addr
    sessions[code] = {'ip': ip, 'time': datetime.utcnow()}
    return jsonify({"status": "ok", "your_ip": ip})

@app.route('/lookup/<code>', methods=['GET'])
def lookup(code):
    session = sessions.get(code)
    if session and datetime.utcnow() - session['time'] < timedelta(minutes=5):
        return jsonify({"ip": session['ip']})
    return jsonify({"error": "Code expired or not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
