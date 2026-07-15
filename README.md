<<<<<<< HEAD
# AI Telephony Proof of Concept

An AI-powered telephony application that enables real-time voice conversations using Google's Gemini Live API and Exotel-compatible media streaming.

## Features

- AI Voice Conversations using Gemini Live API
- Real-time Audio Streaming
- WebSocket-based Communication
- Exotel Media Streaming Support
- Noise Suppression
- DTMF Event Handling
- Automatic Connection Management
- Low Latency Audio Processing

## Tech Stack

### Frontend
- Next.js
- React
- TypeScript

### Backend
- Python
- WebSockets
- Gemini Live API

### Telecom
- Exotel (Media Streaming Compatible)

### Development Tools
- ngrok
- Git
- GitHub

---

## Architecture

```
Caller
      │
      ▼
Exotel
      │
      ▼
WebSocket Server
      │
      ▼
Python Backend
      │
      ▼
Gemini Live API
      │
      ▼
AI Voice Response
```

---

## Project Structure

```
Agent-Stream/
│
├── core/
│   ├── gemini_live_recruiter.py
│   └── ...
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd Agent-Stream

pip install -r requirements.txt

python main.py
```

---

## Environment Variables

Create a `.env` file and configure:

- Gemini API Key
- Gemini Model
- Gemini Voice
- Server Host
- Server Port

---

## Status

- Gemini Live Integration
- Exotel-Compatible WebSocket Server
- AI Audio Streaming
- Real-time Voice Processing
- Production-ready Backend Architecture

---

## Author

Mahalakshmi R K
=======
# AI Telephony POC
>>>>>>> 1732b66 (Updated README)
