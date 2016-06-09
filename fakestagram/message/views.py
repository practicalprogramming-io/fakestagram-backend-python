from flask import Blueprint, request, make_response
from flask.ext.login import login_required, current_user


mod = Blueprint('message', __name__)


@login_required
@mod.route('/messages/<message_id>', methods=['GET'])
def read_message():
    pass

@login_required
@mod.route('/messages/', methods=['POST'])
def send_message():
    pass
