# app.py
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all origins, useful for local development

@app.route('/')
def serve_index():
    """Serves the index.html file."""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serves static files."""
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    # debug=True allows for automatic reloading on code changes
    app.run(debug=True, host='0.0.0.0', port=5000)
