from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse

from core.gemini_client import GeminiClient

app = FastAPI(title="AI Telephony POC")


@app.get("/")
async def home():
    return {"status": "AI Telephony Backend Running"}


@app.get("/answer")
async def answer():
    # Placeholder until Exotel webhook configuration is available
    return {
        "status": "Waiting for Exotel Voice App configuration"
    }


@app.post("/event")
async def event(request: Request):
    body = await request.json()
    print("📞 Exotel Event:", body)
    return {"status": "ok"}


@app.websocket("/media")
async def media(websocket: WebSocket):

    await websocket.accept()

    print("📞 Client Connected")

    gemini = GeminiClient()

    try:
        async with gemini.connect() as session:

            print("🤖 Gemini Live Connected")

            while True:

                message = await websocket.receive()

                print("📩 Received:", message)

                # Exotel audio → Gemini
                # TODO: Send incoming audio to Gemini

                # Gemini audio → Exotel
                # TODO: Receive Gemini audio and send back to Exotel

    except WebSocketDisconnect:
        print("📴 Client Disconnected")

    except Exception as e:
        print(f"❌ Error: {e}")