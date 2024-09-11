#!/usr/bin/env python3
""" encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ expects one string argument name password and returns
        a salted, hashed password, which is a byte string.
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """  expects 2 arguments and returns a boolean.
        Use bcrypt to validate that the provided password
        matches the hashed password.
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
