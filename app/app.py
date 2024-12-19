import os
import json
from flask import Flask, jsonify, render_template
from . import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)

# API route to return data from data.json
@app.route('/api')
def get_data():
    try:
        data_path = os.path.join(app.root_path, 'data', 'data.json')
        with open(data_path, 'r', encoding="utf8") as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data.json"}), 400

# Main route to render index.html
@app.route('/')
def index():
    return render_template('index.html')  # Renders the HTML template

if __name__ == '__main__':
    app.run(debug=True)