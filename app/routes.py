from fastapi import APIRouter
from classes import TelegramBot
from formatter import format_message
from schemas import GithubWebhookRequest

webhook_router = APIRouter()


@webhook_router.post("/github")
async def github_webhook(request: GithubWebhookRequest) -> dict[str, str]:

    message: str = format_message(request)

    TelegramBot(message).send_message()
    # YuchatBot(message).send_message()

    return {"status": "good"}
