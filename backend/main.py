from fastapi import FastAPI, Depends, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from slowapi import Limiter
from slowapi.util import get_remote_address
from structlog import get_logger
from sqlalchemy.orm import Session
from typing import Optional
import backend.crud as crud  # Absolute import
import backend.schemas as schemas  # Absolute import
import backend.database as database  # Absolute import
import backend.auth as auth  # Absolute import
from backend.auth import create_access_token, authenticate_user  # Absolute import

app = FastAPI()
logger = get_logger()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)
    logger.info("Database initialized")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/profile", response_model=schemas.Profile)
@limiter.limit("5/minute")
def create_profile(
    request: Request,
    profile: schemas.ProfileCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(auth.get_current_user)
):
    logger.info("Creating profile", user=current_user)
    return crud.create_profile(db=db, profile=profile)

@app.get("/profile", response_model=schemas.Profile)
def read_profile(db: Session = Depends(database.get_db)):
    profile = crud.get_profile(db)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.put("/profile", response_model=schemas.Profile)
@limiter.limit("5/minute")
def update_profile(
    request: Request,
    profile: schemas.ProfileCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(auth.get_current_user)
):
    logger.info("Updating profile", user=current_user)
    updated = crud.update_profile(db=db, profile_id=1, profile=profile)
    if updated is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated

@app.get("/projects")
def get_projects(
    skill: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(database.get_db)
):
    if skill:
        return crud.get_projects_by_skill(db, skill, skip, limit)
    profile = crud.get_profile(db)
    return profile.projects[skip:skip + limit] if profile else []

@app.get("/skills/top")
def get_top_skills(top_n: int = 3, db: Session = Depends(database.get_db)):
    return crud.get_top_skills(db, top_n)

@app.get("/search")
def search(
    q: str = Query(...),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(database.get_db)
):
    return crud.search_profile(db, q, skip, limit)

@app.get("/ai-insight")
def ai_insight(db: Session = Depends(database.get_db)):
    profile = crud.get_profile(db)
    if not profile:
        return {"insight": "No profile found"}
    top_skill = profile.skills[0] if profile.skills else "N/A"
    return {"insight": f"Based on your top skill '{top_skill}', consider AI projects in ML."}
