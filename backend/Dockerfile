FROM python:3.8-slim-buster

ENV POETRY_VERSION=1.0.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /backend

COPY poetry.lock pyproject.toml /backend/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install

# Creating folders, and files for a project:
COPY . .

ENV PYTHONPATH /backend/src

ENV MODULE_NAME="albot_backend.app"

EXPOSE 2345

CMD ["python", "src/albot_backend/app.py"]



