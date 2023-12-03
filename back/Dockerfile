FROM python:3.12

# Set the working directory in the Docker image
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock files into the image
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

# Copy the rest of the application into the image
COPY . .

ENTRYPOINT ["python", "-m", "app"]
