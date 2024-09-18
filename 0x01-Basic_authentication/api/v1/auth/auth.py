#!/usr/bin/env python3
"""
Auth module for the API
"""
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
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
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