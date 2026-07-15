import asyncio

from core.gemini_client import GeminiClient


async def main():

    client = GeminiClient()

    async with client.connect() as session:

        print("✅ Connected")

        await session.send_client_content(
            turns={
                "role": "user",
                "parts": [
                    {
                        "text": "Introduce yourself as an AI recruiter."
                    }
                ]
            },
            turn_complete=True,
        )

        async for response in session.receive():
            if response.server_content:
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.text:
                            print(part.text)
                        elif part.inline_data:
                            print("🎤 Received Audio Response")


asyncio.run(main())