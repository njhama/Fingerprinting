from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/fingerprint', methods=['POST'])
def fingerprint():
    data = request.json
    combined = '|'.join(str(v) for v in data.values())
    fingerprint = hashlib.sha256(combined.encode()).hexdigest()
    return jsonify({
        "fingerprint": fingerprint,
        "collected_data": data
    })

@app.route('/')
def index():
    return open('index.html').read()

if __name__ == '__main__':
    app.run(debug=True)
