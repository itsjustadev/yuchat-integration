from dotenv import load_dotenv
import os
import httpx


class Bot:
    def __init__(self, message: str) -> None:

        load_dotenv()
        self.message: str = message
        self.BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
        self.CHAT_ID: str | None = os.getenv("CHAT_ID")
        if not self.BOT_TOKEN or not self.CHAT_ID:
            raise ValueError("BOT_TOKEN и CHAT_ID должны быть заданы в actions secrets")

    def send_telegram_message(self) -> None:
        url: str = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"

        response: httpx.Response = httpx.post(
            url,
            data={
                "chat_id": self.CHAT_ID,
                "text": self.message,
                "parse_mode": "HTML",
            },
        )

        print(response.status_code, response.text)
