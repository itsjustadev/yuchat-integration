import os
from classes import TelegramBot, YuchatBot


message: str = (
    f"*CI/CD Build Report*\n\n"
    f"*Build URL:* [Открыть сборку]({os.getenv('BUILD_URL')})\n"
    f"*Branch:* `{os.getenv('BRANCH')}`\n"
    f"*Repository:* `{os.getenv('REPO')}`\n"
    f"*User:* `{os.getenv('USER')}`\n"
    f"*Workflow:* `{os.getenv('WORKFLOW_NAME')}`\n\n"
    f"🧹 *Lint:* ✅ {os.getenv('LINT_RESULT')}\n"
    f"🚀 *Deploy:* ✅ {os.getenv('DEPLOY_RESULT')}\n"
    f"📊 *Get Info:* ✅ {os.getenv('GET_INFO_RESULT')}"
)


TelegramBot(message).send_message()
# YuchatBot(message).send_message()
