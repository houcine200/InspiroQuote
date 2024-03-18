#!/usr/bin/python3
"""Defines the DBStorage engine."""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.quote import Quote
from models.category import Category
from models.author import Author
from models.user import User
from models.review import Review


classes = {
    "Category": Category,
    "Quote": Quote,
    "Author": Author,
    "User": User,
    "Review": Review
}


class DBStorage:
    """Manages the storage of hbnb models in a database."""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor: Initialize the DBStorage class."""
        user = getenv('IQ_MYSQL_USER')
        pwd = getenv('IQ_MYSQL_PWD')
        host = getenv('IQ_MYSQL_HOST')
        db = getenv('IQ_MYSQL_DB')

        db_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('IQ_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        db_objects = {}

        if cls is not None:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                db_objects[key] = obj

        else:
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
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__scoop = scoped_session(session_factory)
        self.__session = self.__scoop()

    def close(self):
        """Close the private session attribute"""
        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None


storage = DBStorage()

storage.reload()
