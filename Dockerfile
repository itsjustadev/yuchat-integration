FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN curl -Ls https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

COPY . .

RUN uv sync