from . import default
from flask import request, jsonify
from ..services.Database import Database

db = Database()

@default.route('/api/register', methods=['POST'])
def new_user():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    group = request.json.get('group')

    db.add_user(name, email, password, group)

    return jsonify(result=True)

@default.route('/api/get_group', methods=['GET'])
def get_group():
    group = request.json.get('group')
    users = db.get_group(group)
    return jsonify(result=users)


