#!/usr/bin/env python3
"""
    Session authentication module
"""
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


# (= POST /api/v1/auth_session/login):
@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Post auth_session/login
    """
    from api.v1.app import auth
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        user_found_bool = user.is_valid_password(password)
        if user.is_valid_password(password):
            user_found = user
    if not user_found_bool:
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user_found.id)
    session_name = getenv("SESSION_NAME")

    response = jsonify(user_found.to_json())
    response.set_cookie(session_name, session_id)
    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /auth_session/logout
    """
    from api.v1.app import auth
    deleted = auth.destroy_session(request)
    if not deleted:
        return abort(404)
    return jsonify({}), 200
