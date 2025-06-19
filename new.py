import os
from dotenv import load_dotenv
import httpx

load_dotenv()

BOT_TOKEN: str | None = os.getenv("BOT_TOKEN")
CHAT_ID: str | None = os.getenv("CHAT_ID")

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

url: str = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response: httpx.Response = httpx.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    },
)

print(response.status_code, response.text)

# print(f"Build url: {os.getenv("BUILD_URL")}")
# print(f"Branch: {os.getenv("BRANCH")}")
# print(f"Repository: {os.getenv("REPO")}")
# print(f"User: {os.getenv("USER")}")
# print(f"Workflow: {os.getenv("WORKFLOW_NAME")}")
# print(f"Lint result: {os.getenv("LINT_RESULT")}")
# print(f"Deploy result: {os.getenv("DEPLOY_RESULT")}")
# print(f"Send info result: {os.getenv("SEND_INFO_RESULT")}")
