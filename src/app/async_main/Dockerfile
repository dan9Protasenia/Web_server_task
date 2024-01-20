FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100
ENV \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true
ENV \
    POETRY_VIRTUALENVS_PATH="/opt/pysetup/.venv" \
    PYSETUP_PATH="/opt/pysetup"
# Final path
ENV PATH="$POETRY_HOME/bin:$POETRY_VIRTUALENVS_PATH/bin:$PATH"



FROM base as builder

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python - --version 1.6.1 \
    && apt-get remove -y curl \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --with server



FROM base as final

COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH

WORKDIR /web

COPY ./ /web

EXPOSE 8002

CMD ["python", "-m", "src.app.async_main.main"]

