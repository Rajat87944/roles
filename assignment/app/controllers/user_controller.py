from flask import Blueprint, jsonify, request
from app import db
from app.models import User
from app.schemas import user_schema, users_schema
from app.services.user_service import create_user, update_user, delete_user

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route("/all", methods=["GET"])
def get_all_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@user_blueprint.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@user_blueprint.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = create_user(data)
    return user_schema.jsonify(new_user), 201

@user_blueprint.route("/<int:id>", methods=["PUT"])
def update_user_route(id):
    data = request.get_json()
    updated_user = update_user(id, data)
    return user_schema.jsonify(updated_user)

@user_blueprint.route("/<int:id>", methods=["DELETE"])
def delete_user_route(id):
    delete_user(id)
    return '', 204
