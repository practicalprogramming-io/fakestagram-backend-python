from flask import Blueprint, request, make_response
from flask.ext.login import login_required, login_user, logout_user, \
    current_user
from fakestagram import db, bcrypt, login_manager


mod = Blueprint('auth', __name__)


@mod.route('/register/', methods=['POST'])
def register():
    pass

@mod.route('/login/', methods=['POST'])
def login():
    pass

@login_required
@mod.route('/logout/', methods=['GET'])
def logout():
    pass
