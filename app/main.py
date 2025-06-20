import os
from classes import TelegramBot, YuchatBot


message: str = (
    f"<b>CI/CD Build Report</b>\n\n"
    f"<b>Build URL:</b> {os.getenv('BUILD_URL')}\n"
    f"<b>Branch:</b> {os.getenv('BRANCH')}\n"
    f"<b>Repository:</b> {os.getenv('REPO')}\n"
    f"<b>User:</b> {os.getenv('USER')}\n"
    f"<b>Workflow:</b> {os.getenv('WORKFLOW_NAME')}\n"
    f"<b>Lint:</b> {os.getenv('LINT_RESULT')}\n"
    f"<b>Deploy:</b> {os.getenv('DEPLOY_RESULT')}\n"
    f"<b>Get Info:</b> {os.getenv('GET_INFO_RESULT')}"
)

TelegramBot(message).send_message()
YuchatBot(message).send_message()
