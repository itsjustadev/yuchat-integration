from dotenv import load_dotenv
import os
import httpx


class Bot:
    def __init__(self, message: str) -> None:

        load_dotenv()

        self.message: str = message
        self.BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
        self.CHAT_ID: str | None = os.getenv("CHAT_ID")
        self.YUCHAT_TOKEN: str | None = os.getenv("YUCHAT_TOKEN")
        self.YUCHAT_CHAT_ID: str | None = os.getenv("YUCHAT_CHAT_ID")

        if not self.BOT_TOKEN or not self.CHAT_ID:
            raise ValueError("BOT_TOKEN и CHAT_ID должны быть заданы в actions secrets")
        if not self.YUCHAT_TOKEN or not self.YUCHAT_CHAT_ID:
            raise ValueError(
                "YUCHAT_TOKEN и YUCHAT_CHAT_ID должны быть заданы в actions secrets"
            )

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

    def send_yuchat_message(self) -> None:
        url: str = "https://yuchat.ai/public/v1/chat.message.send"

        response: httpx.Response = httpx.post(
            url,
            data={
                "workspaceId": "w67Y89gu",
                "chatId": self.YUCHAT_CHAT_ID,
                "markdown": self.message,
            },
        )

        print(response.status_code, response.text)
