# Sync Web Server Task

![Python version](https://img.shields.io/badge/python-3.12.0-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Description
This synchronous web server is designed to handle a variety of network tasks such as servicing HTTP requests, and performing I/O and CPU-bound tasks. It also supports simulating delays and generating random HTTP status codes.

## Technologies
- Python 3.12.0
- `socket` for network communication
- `time` and `random` for timing and randomness control
- `locust` for load testing

## Dependencies
Manage project dependencies using `poetry`. The `poetry.lock` and `pyproject.toml` files contain all necessary dependency information.

<details>
<summary><strong>Installation</strong></summary>
<p>

Install `poetry` if it is not already installed:

```
pip install poetry
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
poetry run python src.sync.main.py
```

</p>
</details>

<details>
<summary><strong>Load Testing</strong></summary>
<p>

For load testing with `locust`, use the `locustfile.py`. Start the tests with the command:

```sh
locust -f locustfile.py
```

</p>
</details>

## Usage
Instructions and examples for using the server can be found in `task.md`.

## Constants
The `constant.py` file contains definitions of constants used throughout the server.
