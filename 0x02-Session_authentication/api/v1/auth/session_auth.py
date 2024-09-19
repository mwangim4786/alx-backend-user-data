#!/usr/bin/env python3

from base64 import b64decode
import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User


class SessionAuth(Auth):
    """ class to handle session auth
    """
