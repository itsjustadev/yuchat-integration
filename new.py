import os

print(f"Build url: {os.getenv("BUILD_URL")}")
print(f"Branch: {os.getenv("BRANCH")}")
print(f"Repository: {os.getenv("REPO")}")
print(f"User: {os.getenv("USER")}")
print(f"Workflow: {os.getenv("WORKFLOW_NAME")}")
print(f"Job '{os.getenv("WORKFLOW_NAME")}' result: {os.getenv("JOB_RESULT")}")
print(f"Deploy result: {os.getenv("DEPLOY_RESULT")}")
