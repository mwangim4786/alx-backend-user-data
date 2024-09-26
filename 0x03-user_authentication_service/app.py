#!/usr/bin/env python3
"""
Module to run flask app
"""
from flask import Flask, jsonify, Response, request, abort
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Home route
    """
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """POST route for user register

    Returns:
        str: messege
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception:
        return jsonify({"messege": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
