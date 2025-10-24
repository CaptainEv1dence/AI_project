FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY backend/ /app/
COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false \
 && poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
