#!/usr/bin/python3
""" Creates user Database table """

from sqlalchemy import Column, String, Integer
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Representation of table user """
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hash_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
