from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Quote(BaseModel, Base):
    __tablename__ = 'quotes'

    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)
    text = Column(String(512), nullable=False)
    author = Column(String(128), nullable=False)
