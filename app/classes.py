from dotenv import load_dotenv
import os
import httpx
from exceptions import TelegramAPIError, YuchatAPIError
from abc import ABC

load_dotenv()


class Bot(ABC):
    def send_message(self) -> None:
        pass


class TelegramBot(Bot):
    def __init__(self, message: str) -> None:
        self.message: str = message
        self.BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
        self.CHAT_ID: str | None = os.getenv("CHAT_ID")
        if not self.BOT_TOKEN or not self.CHAT_ID:
            raise ValueError("BOT_TOKEN и CHAT_ID должны быть заданы в env")

    def send_message(self) -> None:
        url: str = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"

        response: httpx.Response = httpx.post(
            url,
            data={
                "chat_id": self.CHAT_ID,
                "text": self.message,
                "parse_mode": "Markdown",
            },
        )

        print(response.status_code, response.text)
        if response.status_code != 200:
            raise TelegramAPIError(
                f"Telegram API error: {response.status_code} {response.text}"
            )


class YuchatBot(Bot):
    def __init__(self, message: str) -> None:
        self.message: str = message
        self.YUCHAT_TOKEN: str | None = os.getenv("YUCHAT_TOKEN")
        self.YUCHAT_CHAT_ID: str | None = os.getenv("YUCHAT_CHAT_ID")
        self.YUCHAT_WORKSPACE: str | None = os.getenv("YUCHAT_WORKSPACE")

        if not self.YUCHAT_TOKEN or not self.YUCHAT_CHAT_ID:
            raise ValueError("YUCHAT_TOKEN и YUCHAT_CHAT_ID должны быть заданы в env")

    def send_message(self) -> None:
        url: str = "https://yuchat.ai/public/v1/chat.message.send"

        response: httpx.Response = httpx.post(
            url,
            json={
                "workspaceId": self.YUCHAT_WORKSPACE,
                "chatId": self.YUCHAT_CHAT_ID,
                "markdown": self.message,
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {self.YUCHAT_TOKEN}",
            },
        )

        print(response.status_code, response.text)
        if response.status_code != 200:
            raise YuchatAPIError(
                f"Yuchat API error: {response.status_code} {response.text}"
            )
