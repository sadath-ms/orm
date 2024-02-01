from apis_app.dependencies.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String
    )
import sqlalchemy

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, nullable=True)
    password_hash = Column(String)

    