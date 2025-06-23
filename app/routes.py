from fastapi import APIRouter
from classes import TelegramBot, YuchatBot
from formatter import format_message
from schemas import GithubWebhookRequest, GithubWebhookResponse

webhook_router = APIRouter()


@webhook_router.post("/github")
async def github_webhook(request: GithubWebhookRequest) -> GithubWebhookResponse:

    message: str = format_message(request)

    TelegramBot(message).send_message()
    YuchatBot(message).send_message()

    return GithubWebhookResponse(result=True)
