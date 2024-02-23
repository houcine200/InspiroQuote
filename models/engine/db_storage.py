#!/usr/bin/python3
"""Defines the DBStorage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from models.base_model import Base
from models.category import Category
from models.quote import Quote

class DBStorage:
    """Manages the storage of InspiroQuote models in a database."""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor: Initialize the DBStorage class."""
        user = getenv('IQ_MYSQL_USER')
        pwd = getenv('IQ_MYSQL_PWD')
        host = getenv('IQ_MYSQL_HOST')
        db = getenv('IQ_MYSQL_DB')

        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)

        if getenv('IQ_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Query on the current database session."""
        db_objects = {}

        if cls is not None:
            # Query objects of the specified class
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                db_objects[key] = obj

        else:
            # Query all types of objects
            for model_class in Base.__subclasses__():
                table = self.__session.query(model_class).all()
                for obj in table:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    db_objects[key] = obj

        return db_objects

    def new(self, obj):
        """Add the object to the current database session."""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create
        the current database session."""
        Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """Close the private session attribute"""
        self.__session.close()
