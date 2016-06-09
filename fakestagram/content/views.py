from flask import Blueprint, request, make_response
from flask.ext.login import login_required, current_user


mod = Blueprint('content', __name__)


@mod.route('/<username>/', methods=['GET'])
def username():
    pass

@login_required
@mod.route('/content/', methods=['POST'])
def content():
    pass

@login_required
@mod.route('/content/<content_id>/comment/', methods=['POST'])
def comment():
    pass

@mod.route('/content/<content_id>/', methods=['GET'])
def content_id():
    pass
