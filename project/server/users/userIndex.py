from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

index_blueprint = Blueprint('index', __name__)

class IndexAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
        users = db.session.query(User).all()
        responseObject = {
        }
        for instance in users:
            responseObject["id " + str(instance.id)] = "email - " + instance.email + " registered_on - " + str(instance.registered_on) + " admin - " + str(instance.admin)
        print(responseObject)
        return make_response(jsonify(responseObject)), 201


# define the API resources
registration_view = IndexAPI.as_view('register_api')

# add Rules for API Endpoints
index_blueprint.add_url_rule(
    '/users/index',
    view_func=registration_view,
    methods=['GET']
)