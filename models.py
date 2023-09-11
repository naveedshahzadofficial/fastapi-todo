from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship


class Todo(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
