from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):
    __tablename__ = 'categories'

    name = Column(String(128), nullable=False)
    quotes = relationship("Quote",
                            backref="category",
                            cascade="all, delete, delete-orphan")