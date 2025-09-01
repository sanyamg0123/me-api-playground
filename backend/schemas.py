from pydantic import BaseModel
from typing import List, Dict, Optional

class Project(BaseModel):
    title: str
    description: str
    links: Optional[List[str]] = None

class Work(BaseModel):
    company: str
    role: str
    duration: str

class Links(BaseModel):
    github: Optional[str] = None
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None

class ProfileBase(BaseModel):
    name: str
    email: str
    education: str
    skills: List[str]
    projects: List[Project]
    work: List[Work]
    links: Links

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int

    class Config:
        from_attributes = True