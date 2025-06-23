from fastapi import FastAPI
from routes import webhook_router
import uvicorn
import asyncio

app = FastAPI()
app.include_router(webhook_router, prefix="/webhook")


async def initialize_and_start_server() -> None:
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(initialize_and_start_server())
