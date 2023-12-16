FROM python:3.10-slim

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

EXPOSE 8002

CMD ["python", "./main.py"]


