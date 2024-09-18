#!/usr/bin/env python3
"""
    basic_auth module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        value = authorization_header.split(' ')[1]
        return value


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        pass