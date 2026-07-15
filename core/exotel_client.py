from core.call_session import CallSession


class ExotelClient:

    def __init__(self):
        self.active_calls = {}

    def create_session(self, stream_id, websocket=None):

        session = CallSession(stream_id=stream_id)
        session.websocket = websocket

        self.active_calls[stream_id] = session

        return session

    def get_session(self, stream_id):

        return self.active_calls.get(stream_id)

    def remove_session(self, stream_id):

        if stream_id in self.active_calls:
            del self.active_calls[stream_id]

    async def send_audio(self, stream_id, audio_bytes):

        session = self.get_session(stream_id)

        if session is None:
            return

        # Exotel audio streaming will be added later

    async def receive_audio(self, stream_id, audio_bytes):

        session = self.get_session(stream_id)

        if session is None:
            return

        session.append_audio(audio_bytes)

    async def end_call(self, stream_id):

        session = self.get_session(stream_id)

        if session:
            session.update_state("COMPLETED")

        self.remove_session(stream_id)