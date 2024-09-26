#!/usr/bin/env python3
""" Creates user Database table """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ hhash pass using bcrypt """
    encoded_pass = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password, salt)
    return hashed_pass
