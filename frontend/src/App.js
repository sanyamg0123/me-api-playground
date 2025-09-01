import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE = 'http://localhost:8000';  // Change to hosted URL later

function App() {
  const [profile, setProfile] = useState(null);
  const [projects, setProjects] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [skill, setSkill] = useState('');

  const fetchProfile = async () => {
    try {
      const res = await axios.get(`${API_BASE}/profile`);
      setProfile(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchProjectsBySkill = async () => {
    try {
      const res = await axios.get(`${API_BASE}/projects?skill=${skill}`);
      setProjects(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleSearch = async () => {
    try {
      const res = await axios.get(`${API_BASE}/search?q=${searchQuery}`);
      console.log('Search results:', res.data);  // Display in console or UI
      // For simplicity, log; extend to show in UI
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="App">
      <h1>Me-API Playground</h1>
      <button onClick={fetchProfile}>View Profile</button>
      {profile && (
        <div>
          <h2>Profile</h2>
          <p>Name: {profile.name}</p>
          <p>Email: {profile.email}</p>
          <p>Education: {profile.education}</p>
          <p>Skills: {profile.skills.join(', ')}</p>
          <h3>Projects</h3>
          <ul>
            {profile.projects.map((p, i) => (
              <li key={i}>{p.title}: {p.description}</li>
            ))}
          </ul>
          <h3>Work</h3>
          <ul>
            {profile.work.map((w, i) => (
              <li key={i}>{w.company} - {w.role} ({w.duration})</li>
            ))}
          </ul>
          <h3>Links</h3>
          <p>GitHub: <a href={profile.links.github}>{profile.links.github}</a></p>
          <p>LinkedIn: <a href={profile.links.linkedin}>{profile.links.linkedin}</a></p>
          <p>Portfolio: <a href={profile.links.portfolio}>{profile.links.portfolio}</a></p>
        </div>
      )}
      <div>
        <h2>Search by Skill for Projects</h2>
        <input value={skill} onChange={(e) => setSkill(e.target.value)} placeholder="e.g., python" />
        <button onClick={fetchProjectsBySkill}>Search</button>
        <ul>
          {projects.map((p, i) => (
            <li key={i}>{p.title}: {p.description}</li>
          ))}
        </ul>
      </div>
      <div>
        <h2>General Search</h2>
        <input value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} placeholder="e.g., python" />
        <button onClick={handleSearch}>Search</button>
        {/* Results logged to console; add UI display if time */}
      </div>
    </div>
  );
}

export default App;