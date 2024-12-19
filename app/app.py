import os
import json  # Import pre prácu s JSON
from flask import Flask, jsonify  # Import pre jsonify
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

@app.route('/')
def hello_world():  # put application's code here
    return "Hello Tour de App!"
    return "Hello From Furkina Baso!"


@app.route('/api', methods=['GET'])
def api_endpoint():
    data = {"organization": "Student Cyber Games"}
    json_file_path = os.path.join(app.instance_path, 'data.json')

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return jsonify(data)

if __name__ == '__main__':
    app.run()
