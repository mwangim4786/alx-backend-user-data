#!/usr/bin/env python3
""" Creates user Database table """
from uuid import uuid4
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ hhash pass using bcrypt """
    encoded_pass = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(encoded_pass, salt)
    return hashed_pass


def _generate_uuid() -> str:
    """generate uuid

    Returns:
        str: representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """

    """
    def __init__(self) -> None:
        """  """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """  """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashP = _hash_password(password)
        new_user = self._db.add_user(email=email,
                                      hashed_password=hashP.decode("utf-8"))
        self._db
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                encoded_hashed_pass = password.encode()
                user_pass_bytes = existing_user.hashed_password.encode("utf-8")
                return bcrypt.checkpw(encoded_hashed_pass, user_pass_bytes)
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create a new session for user

        Args:
            email (str): email of user

        Returns:
            str: string representation of session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return
