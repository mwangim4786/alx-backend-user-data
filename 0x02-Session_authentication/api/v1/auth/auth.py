#!/usr/bin/env python3
"""
Auth module for the API
"""
from os import getenv
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """ Auth class - manages API Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authorithation check"""
        if path[-1] != '/':
            path += '/'
        # if path and path.endswith('/'):
        #     path += '/'
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        for excluded_path in excluded_paths:
            path_without_astrsk = excluded_path.split('*')[0]
            if path.startswith(path_without_astrsk):
                return False
            # if excluded_path.endswith('*'):
            #     if path.startswith(excluded_path[:1]):
            #         return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization header check"""
        # key = 'Authorization'
        # if request is None or key not in request.headers:
        #     return
        # return request.headers.get(key)
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method"""
        return None

    def session_cookie(self, request=None):
        """ retreives cookie value from request
        """
        if not request:
            return
        session_name = getenv("SESSION_NAME")
        cookie = request.cookies.get(session_name)
        return cookie
