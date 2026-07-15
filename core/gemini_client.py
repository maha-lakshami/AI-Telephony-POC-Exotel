from google import genai
from google.genai import types

from config import Config


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(
            api_key=Config.GEMINI_API_KEY
        )

    def connect(self):
        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            system_instruction="""
You are an AI Recruiter.

Speak naturally.
Keep answers short.
Ask only one interview question at a time.
Be polite.
Wait for the candidate to finish speaking.
Never interrupt.
If the interview finishes, thank the candidate.
"""
        )

        return self.client.aio.live.connect(
            model="gemini-2.5-flash-native-audio-preview-12-2025",
            config=config,
        )