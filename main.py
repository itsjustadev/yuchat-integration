import os
from classes import Bot


message: str = (
    f" <b>CI/CD Build Report</b>\n\n"
    f" <b>Build URL:</b> {os.getenv('BUILD_URL')}\n"
    f" <b>Branch:</b> {os.getenv('BRANCH')}\n"
    f" <b>Repository:</b> {os.getenv('REPO')}\n"
    f" <b>User:</b> {os.getenv('USER')}\n"
    f" <b>Workflow:</b> {os.getenv('WORKFLOW_NAME')}\n"
    f" <b>Lint:</b> {os.getenv('LINT_RESULT')}\n"
    f" <b>Deploy:</b> {os.getenv('DEPLOY_RESULT')}\n"
    f" <b>Send Info:</b> {os.getenv('SEND_INFO_RESULT')}"
)

bot: Bot = Bot(message)

bot.send_telegram_message()
bot.send_yuchat_message()
