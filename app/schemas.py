from pydantic import BaseModel


class GithubWebhookRequest(BaseModel):
    BUILD_URL: str
    BRANCH: str
    REPO: str
    USER: str
    WORKFLOW_NAME: str
    LINT_RESULT: str
    DEPLOY_RESULT: str
    GET_INFO_RESULT: str


class GithubWebhookResponse(BaseModel):
    result: bool
