# app/routes/main/views.py

from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/')
def index():
    return {'status': 200, 'msg': 'success'}
