from sqlalchemy import Column, Integer, String, JSON
from backend.database import Base


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    education = Column(String)
    skills = Column(JSON)
    projects = Column(JSON)
    work = Column(JSON)
    links = Column(JSON)