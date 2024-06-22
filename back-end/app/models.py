from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Any(Base):
    __tablename__ = 'anything'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(100))