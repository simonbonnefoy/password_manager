from sqlalchemy import Column, Integer, String
# from password_manager.database.database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    notes = Column(String)
    last_modified = Column(String)
