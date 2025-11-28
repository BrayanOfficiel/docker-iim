from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Flask!',
        'service': 'flask-app',
        'status': 'running'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    })

@app.route('/info')
def info():
    return jsonify({
        'framework': 'Flask',
        'python_version': sys.version.split()[0],
        'service': 'flask-app'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

