import json
from pathlib import Path
from datetime import datetime


class CallLogger:

    def __init__(self):
        self.log_dir = Path("logs")

        self.log_dir.mkdir(exist_ok=True)

    def save_call(self, session):

        filename = self.log_dir / f"{session.stream_id}.json"

        data = {
            "stream_id": session.stream_id,
            "start_time": datetime.fromtimestamp(session.start_time).isoformat(),
            "call_state": session.call_state,
            "candidate": session.candidate_data,
            "transcript": session.transcript,
            "metadata": session.metadata,
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return filename