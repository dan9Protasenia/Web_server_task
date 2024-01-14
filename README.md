# Async Web Server Task

![Python version](https://img.shields.io/badge/python-3.12.0-blue.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Description
This asynchronous web server is designed to handle concurrent network tasks efficiently using `asyncio` and `aiohttp`. It provides endpoints for various asynchronous operations, such as echoing JSON data, performing CPU-bound calculations, and simulating I/O-bound delays.

## Technologies
- Python 3.12.0
- `socket` for network communication
- `time` and `random` for timing and randomness control
- `locust` for load testing
- `aiohttp` for asynchronous HTTP server functionality
- `Docker` for containerization and easy deployment
  
## Dependencies
Dependencies are managed with `poetry`. The `poetry.lock` and `pyproject.toml` files maintain all necessary dependency information.

## Containerization with Docker
This project is containerized with Docker, enabling consistent development environments and deployment workflows.

### Building the Docker Image
To build a Docker image for the project, navigate to the project's root directory and run:
```sh
docker build -t async-app .
```

### Running the Server with Docker
After building the image, you can run the server in a Docker container using:
```sh
docker run -p 8002:8002 async-app
```
This will map the container's port 8002 to port 8002 on your host machine, making the server accessible via `localhost:8000`.

## Usage
Instructions and examples for using the server can be found in `task.md`.

## Constants
The `constants.py` file contains definitions of constants used throughout the server.
