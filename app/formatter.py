from schemas import GithubWebhookRequest


def format_message(data: GithubWebhookRequest) -> str:
    return (
        f"*CI/CD Build Report*\n\n"
        f"*Build URL:* [{data.BUILD_URL}]({data.BUILD_URL})\n"
        f"*Branch:* `{data.BRANCH}`\n"
        f"*Repository:* `{data.REPO}`\n"
        f"*User:* `{data.USER}`\n"
        f"*Workflow:* `{data.WORKFLOW_NAME}`\n\n"
        f"*Jobs:*\n"
        f"*Lint:* {data.LINT_RESULT}\n"
        f"*Deploy:* {data.DEPLOY_RESULT}\n"
        f"*Get Info:* {data.GET_INFO_RESULT}"
    )
