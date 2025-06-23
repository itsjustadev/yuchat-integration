import os
from fastapi import APIRouter, Request
from classes import TelegramBot, YuchatBot
from formatter import format_message
from schemas import GithubWebhookRequest

webhook_router = APIRouter()


@webhook_router.post("/github")
async def github_webhook(request: GithubWebhookRequest) -> dict[str, str]:

    message: str = format_message(request)

    TelegramBot(message).send_message()
    YuchatBot(message).send_message()

    return {"status": "ok"}
