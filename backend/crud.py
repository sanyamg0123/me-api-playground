from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional
import json

def get_profile(db: Session, profile_id: int = 1):  # Assume single profile ID=1
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def update_profile(db: Session, profile_id: int, profile: schemas.ProfileCreate):
    db_profile = get_profile(db, profile_id)
    if db_profile:
        for key, value in profile.dict().items():
            setattr(db_profile, key, value)
        db.commit()
        db.refresh(db_profile)
    return db_profile

# Query helpers
def get_projects_by_skill(db: Session, skill: str, skip: int = 0, limit: int = 10):
    profile = get_profile(db)
    if not profile:
        return []
    projects = [p for p in profile.projects if skill.lower() in p.get('description', '').lower()]
    return projects[skip:skip + limit]

def get_top_skills(db: Session, top_n: int = 3):
    profile = get_profile(db)
    if not profile:
        return []
    return sorted(profile.skills, key=len, reverse=True)[:top_n]

def search_profile(db: Session, q: str, skip: int = 0, limit: int = 10):
    profile = get_profile(db)
    if not profile:
        return {}
    q_lower = q.lower()
    results = {
        'name': profile.name if q_lower in profile.name.lower() else None,
        'education': profile.education if q_lower in profile.education.lower() else None,
        'skills': [s for s in profile.skills if q_lower in s.lower()],
        'projects': [p for p in profile.projects if q_lower in json.dumps(p).lower()],
        'work': [w for w in profile.work if q_lower in json.dumps(w).lower()],
    }
    for key in ['skills', 'projects', 'work']:
        if isinstance(results[key], list):
            results[key] = results[key][skip:skip + limit]
    return {k: v for k, v in results.items() if v}