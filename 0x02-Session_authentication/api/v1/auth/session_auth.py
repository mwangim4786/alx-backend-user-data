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
