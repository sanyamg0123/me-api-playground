from database import SessionLocal, engine, Base  # Add Base import
from models import Profile
from schemas import Project, Work, Links

def seed_data():
    # Create tables defined in models
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    if db.query(Profile).first():
        print("Data already seeded")
        return
    profile = Profile(
        name="Priyanshu Raj",
        email="priyanshurpr.ug22.cs@nitp.ac.in",
        education="B.Tech in Computer Science, NIT Patna, 2022-2026",
        skills=["Python", "C++", "JavaScript", "HTML/CSS", "Scikit-learn", "TensorFlow", "NLTK", "Pandas", "NumPy", "Matplotlib", "React.js", "Node.js", "Streamlit", "Bootstrap", "Firebase (Auth, Firestore)", "REST APIs", "Firebase", "MongoDB", "SQL", "Git", "VS Code", "Jupyter Notebook", "OpenCV", "Google Calendar API", "Google Gemini API"],
        projects=[
            {
                "title": "XploreMonk",
                "description": "Developed an AI-powered travel planning platform that generates personalized travel itineraries.",
                "links": ["https://github.com/sanyamg0123/xploremonk"]
            },
            {
                "title": "TailorTalk",
                "description": "Developed an AI-powered scheduling assistant using Streamlit and Google Gemini to manage Google Calendar via natural language.",
                "links": ["https://github.com/sanyamg0123/tailortalk"]
            },
        ],
        work=[
            {"company": "Innovate Intern", "role": "Intern", "duration": "May 2025-July 2025"},
        ],
        links={
            "github": "https://github.com/sanyamg0123",
            "linkedin": "https://linkedin.com/in/priyanshuraj16",
            "portfolio": None
        }
    )
    db.add(profile)
    db.commit()
    print("Data seeded")

if __name__ == "__main__":
    seed_data()