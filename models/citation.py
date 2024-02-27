from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Citation(BaseModel, Base):
    __tablename__ = 'citations'

    author_id = Column(String(60), ForeignKey('authors.id'), nullable=False)
    text = Column(String(512), nullable=False)
    
