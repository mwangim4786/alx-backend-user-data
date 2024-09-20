#!/usr/bin/env python3
"""
    session_auth module for the API
"""
from base64 import b64decode
import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User


class SessionAuth(Auth):
    """ class to handle session auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """  creates a Session ID for a user_id
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return use_id from session_id
        """
        if not session_id or not isinstance(session_id, str):
            return
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """  returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        if not session_id:
            return

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Logout user - Delete user session
        """
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        user = User.get(user)
        if not user:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except KeyError:
            pass
        return True
