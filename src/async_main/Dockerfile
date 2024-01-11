FROM python:3.10-slim

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.7.1
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

EXPOSE 8002

CMD ["python", "./main.py"]
