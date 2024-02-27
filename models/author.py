from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Author(BaseModel, Base):
    __tablename__ = 'authors'

    name = Column(String(128), nullable=False)
    citations = relationship("Citation",
                            backref="author",
                            cascade="all, delete, delete-orphan")
