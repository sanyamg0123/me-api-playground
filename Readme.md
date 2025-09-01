# ME API Playground

A full-stack application featuring a React frontend and FastAPI backend, designed to showcase your profile, skills, and projects.

## 🚀 Live Demo

* **Frontend (Vercel):** [https://me-api-playground-silk.vercel.app/](https://me-api-playground-silk.vercel.app/)
* **Backend (Render):** [https://me-api-playground-4-35m3.onrender.com/](https://me-api-playground-4-35m3.onrender.com/)

## 🐄 Resume

View my resume here: [https://drive.google.com/file/d/1qZ2Wa5UjvFitxWjmxvJ6yZTUbJ\_Ma7zk/view?usp=sharing](https://drive.google.com/file/d/1qZ2Wa5UjvFitxWjmxvJ6yZTUbJ_Ma7zk/view?usp=sharing)

## 🔧 Technologies Used

* **Frontend:** React, Axios
* **Backend:** FastAPI, SQLAlchemy, PostgreSQL
* **Deployment:** Vercel (Frontend), Render (Backend)

## ⚙️ Setup Instructions

### Frontend

1. Clone the repository:

   ```bash
   git clone https://github.com/sanyamg0123/me-api-playground.git
   cd me-api-playground/frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

   The app will run at [http://localhost:3000](http://localhost:3000).

### Backend

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at [http://localhost:8000](http://localhost:8000).

## 📜 API Endpoints

* **GET /profile:** Retrieve user profile
* **POST /profile:** Create a new profile
* **PUT /profile:** Update existing profile
* **GET /projects:** List projects
* **GET /skills/top:** Get top skills
* **GET /search:** Search profiles
* **GET /ai-insight:** Get AI insights

## 📚 Documentation

The API is documented using Swagger UI. Access it at:

[http://localhost:8000/docs](http://localhost:8000/docs)
