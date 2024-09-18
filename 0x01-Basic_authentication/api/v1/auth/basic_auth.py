#!/usr/bin/env python3
"""
    basic_auth module for the API
"""
from base64 import b64decode
import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User


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
    

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        user, password = decoded_base64_authorization_header.split(":")
        return user, password
    

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        
        try:
            users = User.search(attributes={"email": user_email})
        except KeyError:
            return None
        except Exception:
            return None
        
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
    

    def current_user(self, request=None) -> TypeVar('User'):
        """sumary_line
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        auth_header = self.authorization_header(request)
        b64_str = self.extract_base64_authorization_header(auth_header)
        decoded_b64_str = self.decode_base64_authorization_header(b64_str)
        email, password = self.extract_user_credentials(decoded_b64_str)
        user = self.user_object_from_credentials(email, password)
        return user
