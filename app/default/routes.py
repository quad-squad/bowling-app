from . import default
from flask import request, Response, jsonify
from ..services.Database import Database

db = Database()

@default.route('/api/register', methods=['POST'])
def new_user():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    group = request.json.get('group')

    db.add_user(name, email, password, group)

    print(db.get_users())

    return jsonify(result=True)
