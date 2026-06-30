# 🚀 GoalMint AI

### AI-Powered Productivity Companion

**Turn Goals Into Actionable Success Plans with AI-Generated Roadmaps and Smart Task Planning.**

---

## 🌐 Live Demo

**Live Application:**  
https://goalmint-ai.onrender.com

## 💻 GitHub Repository

**Source Code:**  
https://github.com/mohdmuzaffar9/goalmint-AI

---

# 📖 Project Overview

GoalMint AI is an AI-powered productivity companion developed for the **Vibe2Ship Hackathon** under the problem statement **"The Last-Minute Life Saver."**

Traditional productivity applications mainly depend on reminders and notifications. While reminders inform users about upcoming deadlines, they rarely help users understand **how to complete their goals**. As a result, users often procrastinate, struggle with planning, and miss important deadlines.

GoalMint AI solves this challenge by transforming user goals into structured execution plans using **Google Gemini AI**. Instead of simply reminding users about their goals, the application automatically generates an intelligent **six-phase roadmap**, followed by **AI-generated actionable tasks** for each phase.

Users can review, edit, and personalize every AI-generated roadmap and task before saving them, ensuring that AI works as an intelligent assistant rather than replacing human decision-making.

The application also includes secure authentication, goal management, task tracking, AI insights, profile management, and optimized API usage, making it a complete productivity platform for students, professionals, and entrepreneurs.

---

# 🎯 Problem Statement

## **The Last-Minute Life Saver**

### Background

Students, professionals, and entrepreneurs frequently miss deadlines, assignments, meetings, interviews, and important commitments. Most productivity applications rely only on passive reminders, which users often ignore.

### Challenge

Build an AI-powered productivity companion that proactively helps users plan, prioritize, and complete their work before deadlines are missed.

The solution should go beyond simple reminders and focus on helping users take meaningful action through intelligent planning.

### Our Solution

GoalMint AI combines Artificial Intelligence with practical productivity features by converting user goals into structured six-phase roadmaps and AI-generated tasks. Instead of simply notifying users, the platform helps them understand **what to do**, **when to do it**, and **how to achieve their goals** through personalized AI guidance.

---

# ✨ Key Highlights

- 🤖 AI-powered Goal Roadmap Generation
- 🗂️ AI-generated Actionable Tasks
- 🎯 Goal Management System
- 📊 Dashboard with Productivity Overview
- 💡 AI Insights
- 🔐 Secure User Authentication
- ✏️ Editable AI-generated Roadmaps & Tasks
- ⚡ Optimized Gemini API Usage
- 🐳 Dockerized Deployment
- ☁️ Successfully Deployed on Render                                                                                            # ✨ Features

## 🤖 AI-Powered Goal Roadmap

GoalMint AI uses **Google Gemini AI** to analyze user goals and automatically generate a structured **6-phase roadmap**, making large goals easier to understand and achieve.

---

## ✅ AI Task Generation

Each roadmap phase can generate **AI-powered actionable tasks** that guide users step by step. Users can edit every generated task before saving.

---

## 🎯 Goal Management

Users can efficiently:

- Create Goals
- View Goals
- Edit Goals
- Delete Goals
- Track Progress

All goals are organized in one centralized dashboard.

---

## 📊 Smart Dashboard

The dashboard provides a quick overview of:

- Active Goals
- Goal Progress
- Productivity Statistics
- AI Insights
- Quick Navigation

---

## 💡 AI Insights

GoalMint AI provides personalized productivity insights to help users stay focused and continuously improve their progress.

---

## 🔐 Secure Authentication

The application includes a complete authentication system with:

- User Registration
- Secure Login
- Session Management
- User Profiles

---

## ✏️ Editable AI Content

Unlike many AI tools, GoalMint AI allows users to edit both AI-generated roadmaps and tasks before saving them, giving users complete control over their plans.

---

## ⚡ Optimized AI Requests

To improve performance and reduce unnecessary API usage:

- Roadmaps are stored in the database
- Tasks are stored after generation
- Repeated AI requests are avoided
- API rate limiting is implemented

---

# 📱 Application Screenshots

## 📸 Dashboard

![](screenshots/dashboard-Screenshot%202026-06-29%20144533.png)

## 🎯 Create Goal

![](screenshots/Screenshot%202026-06-30%20165313.png)

## 📋 My Goals

![](screenshots/Mygoals-Screenshot%202026-06-29%20142050.png)

## 🗺️ AI Roadmap

![](screenshots/roadmap-Screenshot%202026-06-29%20140615.png)

## ✅ Tasks

![](screenshots/tasks-Screenshot%202026-06-29%20140754.png)

## 🤖 AI Insights

![](screenshots/ai-insights-Screenshot%202026-06-29%20142116.png)

## 👤 Profile

![](screenshots/profile-Screenshot%202026-06-29%20142146.png)

## ✏️ Edit Goal

![](screenshots/editgaols-Screenshot%202026-06-29%20140907.png)


# 🔄 System Workflow

User Login / Register
          │
          ▼
      Dashboard
          │
          ▼
     Create Goal
          │
          ▼
 Google Gemini AI
          │
          ▼
Generate 6-Phase Roadmap
          │
          ▼
User Reviews & Edits
          │
          ▼
 Save Roadmap
          │
          ▼
 Generate AI Tasks
          │
          ▼
User Reviews & Edits
          │
          ▼
 Save Tasks
          │
          ▼
Track Progress from Dashboard

---

# 🧠 AI Workflow

User Goal
     │
     ▼
Google Gemini AI
     │
     ▼
Generate 6-Phase Roadmap
     │
     ▼
User Reviews & Edits
     │
     ▼
Store in Database
     │
     ▼
Generate AI Tasks
     │
     ▼
User Reviews & Edits
     │
     ▼
Save Tasks                                                            # 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| **Programming Language** | Python |
| **Backend Framework** | Django |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap 5 |
| **Database** | SQLite |
| **Artificial Intelligence** | Google Gemini AI |
| **Authentication** | Django Authentication System |
| **Static File Management** | WhiteNoise |
| **Deployment** | Docker, Gunicorn, Render |
| **Version Control** | Git & GitHub |

---

# 📂 Project Structure


GoalMint-AI/
│
├── accounts/
├── ai_engine/
├── analytics/
├── core/
├── goals/
├── notifications/
├── tasks/
│
├── config/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── media/
│
├── Dockerfile
├── start.sh
├── manage.py
├── requirements.txt
├── .dockerignore
└── README.md

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mohdmuzaffar9/goalmint-AI.git

cd goalmint-AI
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

GEMINI_API_KEY=your_gemini_api_key
```

---

## 5️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 🐳 Docker Deployment

Build Docker Image

```bash
docker build -t goalmint-ai .
```

Run Container

```bash
docker run -p 8080:8080 goalmint-ai
```

---

# ☁️ Production Deployment

GoalMint AI is successfully deployed using:

- Docker
- Gunicorn
- Render

Live Demo:

https://goalmint-ai.onrender.com

---

# 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django Secret Key |
| `DEBUG` | Debug Mode |
| `GEMINI_API_KEY` | Google Gemini API Key |

---

# 🚀 Performance Optimizations

- AI-generated roadmaps are stored in the database.
- AI-generated tasks are stored after generation.
- API rate limiting reduces unnecessary requests.
- WhiteNoise efficiently serves static files.
- Docker ensures consistent deployment.
- Gunicorn provides a production-ready WSGI server.                             # 📈 Current Limitation

During development, we identified one important limitation in the current workflow.

At present, whenever a user creates a goal, GoalMint AI automatically generates a complete **6-phase roadmap** and AI-powered tasks.

This works well for long-term goals such as:

- Learning a new skill
- Placement preparation
- Building a startup
- Exam preparation

However, for simple activities such as:

- Attend a meeting at 5 PM
- Pay electricity bill
- Call a client
- Submit an assignment tomorrow

users only require a reminder instead of a complete roadmap.

This limitation has been identified and a future AI enhancement has already been designed.

---

# 🚀 Future Improvements

The next version of GoalMint AI will introduce an **AI Intent Analyzer**.

Instead of directly generating a roadmap, the AI will first understand the user's intent and decide the most appropriate action.

| User Input | AI Decision | Output |
|------------|------------|--------|
| Attend Meeting at 5 PM | Reminder | Smart Reminder |
| Learn DSA | Long-Term Goal | AI Roadmap + Tasks |
| Crack Placements | Career Goal | AI Roadmap + Tasks |
| Exercise Daily | Habit | Habit Tracker |
| Build Portfolio | Project | AI Roadmap + Tasks |

---

## Planned Features

- 🧠 AI Intent Analyzer
- 📅 Google Calendar Integration
- 📧 Email Reminder System
- 🔔 Smart Push Notifications
- 📱 WhatsApp & Telegram Notifications
- 🎤 Voice Assistant Support
- 📊 Advanced Productivity Analytics
- 🤖 AI-Based Task Prioritization
- 📈 Personalized Productivity Recommendations
- ☁️ PostgreSQL Cloud Database
- 👥 Team Collaboration & Shared Goals

---

# 👨‍💻 Developer

**Mohammed Muzaffar**

Computer Science & Engineering Student

Passionate about AI, Backend Development, Django and Building Real-World Products.

### Connect with me

- GitHub: https://github.com/mohdmuzaffar9
- LinkedIn: https://www.linkedin.com/in/mohammed-muzaffar-3b61572a4

---

# 📄 License

This project is developed for educational purposes as part of the **Vibe2Ship Hackathon**.

---

# ⭐ Support

If you found this project useful, consider giving the repository a **Star ⭐** on GitHub.

It motivates future development and helps others discover the project.

---

# 🙏 Acknowledgements

Special thanks to:

- Google Gemini AI
- Django Community
- Render
- Vibe2Ship Hackathon
- Coding Ninjas
