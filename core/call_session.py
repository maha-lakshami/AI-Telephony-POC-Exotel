from dataclasses import dataclass, field
from typing import Dict, Any
import time


@dataclass
class CallSession:
    stream_id: str

    start_time: float = field(default_factory=time.time)

    sample_rate: int = 16000

    websocket = None

    gemini_session = None

    audio_buffer: bytes = b""

    transcript: str = ""

    candidate_data: Dict[str, Any] = field(default_factory=dict)

    call_state: str = "CONNECTED"

    metadata: Dict[str, Any] = field(default_factory=dict)

    def update_state(self, state: str):
        self.call_state = state

    def append_audio(self, chunk: bytes):
        self.audio_buffer += chunk

    def clear_audio(self):
        self.audio_buffer = b""

    def add_transcript(self, text: str):
        self.transcript += text + "\n"

    def save_candidate(self, key: str, value):
        self.candidate_data[key] = value