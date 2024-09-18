#!/usr/bin/env python3
"""
    basic_auth module for the API
"""
from base64 import b64decode
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
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        
        try:
            encodeed_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encodeed_base64.decode('utf-8')
        except Exception:
            return
        return decoded_base64
