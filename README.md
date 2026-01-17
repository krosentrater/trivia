A full‑stack trivia experience built with a Flask backend, React/Vite frontend, and the Open Trivia Database API. Designed with clean architecture, maintainability, and contributor clarity at its core.
✨ Features
- 🔌 Flask API backend for categories, questions, and scoring
- ⚡ React + Vite frontend with modular components and clean routing
- 🎨 Playful, inviting UI using rounded fonts and colorful category tiles
- 📚 Fully documented architecture for easy onboarding
- 🌐 Integrates with Open Trivia DB for real‑time questions
- 🧪 Testing‑friendly structure for both backend and fronten

/trivia-app
│
├── trivia/        # Flask API
│   ├── trivia/            # App package
│   │   ├── __init__.py
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── venv/
│   └── run.py
│
└── trivia-frontend/       # React + Vite app
    ├── src/
    │   ├── components/
    │   ├── pages/
    │   ├── services/
    │   ├── styles/
    │   └── App.jsx
    ├── public/
    └── vite.config.js
