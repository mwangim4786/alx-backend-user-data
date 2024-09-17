#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
         """ require authorithation check"""
         return False

    def authorization_header(self, request=None) -> str:
        """ authorization header check"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method"""
        return None