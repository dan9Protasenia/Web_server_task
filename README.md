# Web Server Task

![Python version](https://img.shields.io/badge/python-3.12.0-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)

## Description
This web server project includes both synchronous and asynchronous servers. The synchronous server handles network tasks such as servicing HTTP requests, performing I/O and CPU-bound tasks, and simulating delays and generating random HTTP status codes. The asynchronous server, using `asyncio` and `aiohttp`, is designed to handle concurrent network tasks efficiently and provides endpoints for various asynchronous operations.

![Python version](https://img.shields.io/badge/python-3.12.0-blue.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Description
This asynchronous web server is designed to handle concurrent network tasks efficiently using `asyncio` and `aiohttp`. It provides endpoints for various asynchronous operations, such as echoing JSON data, performing CPU-bound calculations, and simulating I/O-bound delays.

## Technologies
- Python 3.12.0
- `socket` for synchronous network communication
- `aiohttp` for asynchronous HTTP server functionality
- `time` and `random` for timing and randomness control
- `locust` for load testing
- `Docker` for containerization and easy deployment

## Dependencies
Manage project dependencies using `poetry`. The `poetry.lock` and `pyproject.toml` files contain all necessary dependency information.

<details>
<summary><strong>Installation</strong></summary>
<p>

Install `poetry` if it is not already installed:

```
curl -sSL https://install.python-poetry.org | python - --version 1.7.1
```

Clone the repository and navigate to its directory:

```sh
git clone https://github.com/dan9Protasenia/Web_server_task
cd Web_server_task
```

Then install the dependencies:

```sh
poetry install
```

</p>
</details>

<details>
<summary><strong>Running the Server</strong></summary>
<p>

To start the server, use the command:

```sh
poetry run python -m src.synс.main
```

</p>
</details>

<details>
<summary><strong>Load Testing</strong></summary>
<p>

For load testing with `locust`, use the `locustfile.py`. Start the tests with the command:

```sh
poetry run locust -f locustfile.py
```
Or, you can activate the virtual environment shell provided by Poetry and run Locust from there:

```sh
poetry shell
locust -f locustfile.py
```
</p>
</details>

##Running the Server  

## Containerization with Docker
This project is containerized with Docker, enabling consistent development environments and deployment workflows.

### Building the Docker Image for the Synchronous Server
To build a Docker image for the project, navigate to the project's root directory and run:
```sh
docker build -t sync-app .
```

### Running the Server with Docker
After building the image, you can run the server in a Docker container using:
```sh
docker run -p 8001:8001 sync-app
```
This will map the container's port 8001 to port 8001 on your host machine, making the server accessible via `localhost:8001`.

### Building the Docker Image for the Asynchronous Server
To build a Docker image for the project, navigate to the project's root directory and run:
```sh
docker build -t async-app .
```

### Running the Server with Docker
After building the image, you can run the server in a Docker container using:
```sh
docker run -p 8002:8002 async-app
```
This will map the container's port 8002 to port 8002 on your host machine, making the server accessible via `localhost:8002`.

## Usage
Instructions and examples for using the server can be found in `task.md`.

## Constants
The `constant.py` file contains definitions of constants used throughout the server.

