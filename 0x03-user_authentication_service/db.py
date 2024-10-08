#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add user method
        """
        if not email or not hashed_password:
            return
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ gets user id based on keywords provided """
        for key in kwargs.keys():
            if not hasattr(User, key):
                raise InvalidRequestError()
        user = self._session.query(User).filter_by(**kwargs).first()

        if user:
            return user
        raise NoResultFound()

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update user attributes based on keywords provided """
        user_to_update = self.find_user_by(id=user_id)
        for attr, value in kwargs.items():
            if hasattr(User, attr):
                setattr(user_to_update, attr, value)
            else:
                raise ValueError()
        self.__session.commit()
