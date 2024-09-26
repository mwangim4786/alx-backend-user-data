#!/usr/bin/env python3
""" Creates user Database table """
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ hhash pass using bcrypt """
    encoded_pass = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(encoded_pass, salt)
    return hashed_pass


class Auth:
    """

    """
    def __init__(self) -> None:
        """  """
        self.__db = DB()

    def register_user(self, email: str, password: str) -> User:
        """  """
        try:
            existing_user = self.__db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hash_pass = _hash_password(password)
        new_user = self.__db.add_user(email=email,
                                      hashed_p=hash_pass.decode("utf-8"))
        self.__db
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login
        """
        try:
            existing_user = self.__db.find_user_by(email=email)
            if existing_user:
                encoded_hashed_pass = password.encode()
                user_pass_bytes = existing_user.hashed_password.encode("utf-8")
                return bcrypt.checkpw(encoded_hashed_pass, user_pass_bytes)
            else:
                return False
        except NoResultFound:
            return False
