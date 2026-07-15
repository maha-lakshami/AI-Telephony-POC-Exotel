# AI Telephony Proof of Concept

An AI-powered telephony backend that enables real-time voice conversations using **Google Gemini Live API**, **FastAPI**, and **Exotel-compatible media streaming**.

---

# Features

- Google Gemini Live API Integration
- AI-powered Voice Conversations
- FastAPI Backend
- WebSocket-based Communication
- Exotel-Compatible Media Streaming Foundation
- Real-time Audio Processing
- Conversation Management
- Call Session Management
- Modular Project Architecture
- Low Latency Communication

---

# Tech Stack

## Backend

- Python 3.11
- FastAPI
- WebSockets
- Google Gemini Live API

## Telecom

- Exotel (Media Streaming Compatible)

## Development Tools

- Uvicorn
- Git
- GitHub
- ngrok

---

# Architecture

```
Caller
   │
   ▼
Exotel
   │
   ▼
FastAPI WebSocket Server
   │
   ▼
Gemini Live API
   │
   ▼
AI Voice Response
```

---

# Project Structure

```
AI-Telephony-POC-Exotel/
│
├── core/
│   ├── audio_processor.py
│   ├── bot_framework.py
│   ├── bot_launcher.py
│   ├── call_session.py
│   ├── conversation_manager.py
│   ├── exotel_client.py
│   ├── gemini_client.py
│   ├── gemini_live_recruiter.py
│   ├── logger.py
│   └── openai_realtime_sales_bot.py
│
├── engines/
│
├── app.py
├── config.py
├── main.py
├── requirements.txt
├── env.example
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/maha-lakshami/AI-Telephony-POC-Exotel.git
```

Move into the project folder

```bash
cd AI-Telephony-POC-Exotel
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m uvicorn app:app --reload
```

---

# Environment Variables

Create a `.env` file based on `env.example`

```env
GEMINI_API_KEY=YOUR_API_KEY
COMPANY_NAME=JobForm Automator
SALES_BOT_NAME=AI Recruiter
SERVER_HOST=0.0.0.0
SERVER_PORT=5000
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health Check |
| GET | `/answer` | Voice Webhook (Placeholder) |
| POST | `/event` | Event Callback |
| WebSocket | `/media` | Audio Streaming |

---

# Current Status

### Completed

- FastAPI Backend
- Google Gemini Live API Integration
- WebSocket Communication
- AI Conversation Framework
- Conversation Manager
- Call Session Management
- Audio Processing Modules

### In Progress

- Exotel Voice Integration
- Real-time Phone Call Testing
- End-to-End AI Calling Workflow

---

# Author

**Mahalakshmi R K**

GitHub: https://github.com/maha-lakshami

---

# License

This project is developed as an AI Telephony Proof of Concept for learning and demonstration purposes.
