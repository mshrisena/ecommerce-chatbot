# 🛒 Ecommerce Chatbot Application

This is a full-stack chatbot application built with Flask and vanilla JavaScript. It enables users to log in, chat with an AI assistant, retrieve chat history, and even send voice messages. It’s designed for ecommerce support scenarios such as answering customer queries, guiding product searches, and simulating assistance workflows.

---

## 🚀 Features

- 🔐 User login/logout with persistent session via `localStorage`
- 💬 Real-time chat interface with async bot responses
- 📚 Chat history retrieval per user
- 🎙️ Voice-to-text chat via Web Speech API
- ✅ Modular Flask backend with route separation

---

## 🧱 Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Frontend   | HTML, CSS, JavaScript    |
| Backend    | Python, Flask, Flask-CORS |
| Communication | REST API (`fetch`)   |
| Storage    | Local or in-memory (extendable to DB) |
| Voice Input | Web Speech API         |

---

## 📦 Folder Structure
ecommerce/ ├── backend/ │  
                 ├── app.py │   
                 └── routes/ 
                       ├── chat.py       
                       ├── auth.py       
                       ├── history.py 
                       └── search.py
           ├── frontend/ 
                  ├── index.html 
                  ├── style.css 
                  └── app.js 
           ├── requirements.txt
           └── README.md


---

## 🛠️ Setup & Run

### 🔹 Backend

1. Navigate to the backend:
 
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
2.- Run the server (on port 5001):
   python app.py
 
 
Frontend
Open frontend/index.html in a browser. For best results, use Live Server or run from localhost.

Key Learnings
- Setting up CORS for safe cross-origin communication
- Structuring Flask apps using blueprints
- Debugging frontend-backend sync issues (reload loops, fetch errors)
- Integrating speech recognition into a dynamic JS interface

 Future Scope
- Integrate with a real product database
- Deploy on cloud platforms (e.g. Render, Vercel, or Heroku)
- Implement JWT or OAuth authentication
- Add feedback and rating functionality

  Author
M.SHRISENA
Built with passion and persistence 








