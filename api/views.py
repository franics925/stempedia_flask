from flask import Blueprint, jsonify
api = Blueprint('api', __name__)


## Post Routes
@api.route('/api/add_post', methods=['POST'])
def add_post():
    return 'Connected', 201

@api.route('/api/posts', methods=['GET'])
def posts():
    posts = []
    return jsonify({'posts': posts})

## Category Routes
@api.route('/api/categories', methods=['GET'])
def categories():
    categories = []
    return jsonify({'categories': categories})

@api.route('/api/add_category', methods=['POST'])
def add_category():
    return 'Connected', 201


## User Routes
@api.route('/api/users', methods=['GET'])
def users():
    users = []
    return jsonify({'users': users})



@api.route('/api/add_comment', methods=['POST'])
def add_comment():
    return 'Connected', 201


