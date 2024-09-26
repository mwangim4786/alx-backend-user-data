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


@app.route("/users", methods=["POST"])
def user() -> str:
    """
    Registers users
    """
    if request.method == "POST":
        raw_email = request.form.get("email")
        email = raw_email.strip()
        raw_pass = request.form.get("password")
        password = raw_pass.strip()
        try:
            AUTH.register_user(email, password)
            message = jsonify({"email": email, "message": "user created"})
            return message
        except Exception:
            return jsonify({"message": "email already registered"})
    else:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
