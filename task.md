# Sync and Async Web Server


## Objective
Develop web servers in Python in 2 versions: a first simple synchronous (sync) web server using only the `socket` module and second an asynchronous (async) web server using the `aiohttp` framework.


### Requirements:
1. **Synchronous (Sync) Web Server:**
    - Create a simple synchronous web server using the `socket` module.
    - The sync server should listen on `localhost` at port _8001_.
    - Implement a single route _/hello_ that responds with a plain text message "Hello, World!".
    - Demonstrate handling HTTP requests synchronously.

2. **Asynchronous (Async) Web Server:**
    - Create an asynchronous web server using the `aiohttp` framework.
    - The async server should listen on `localhost` at port _8002_.
    - Implement two routes:
      + Route 1: _/hello_ - Respond with a plain text message "Hello, World!".
      + Route 2: _/echo_ - Accept POST requests. Respond with the JSON representation of the received POST data.
    - Use asynchronous programming features provided by `aiohttp`.
    - Demonstrate the use of asynchronous functions, `asyncio`, and the `aiohttp` library to handle requests concurrently.

3. **External API:**
    - Create a `package` in _core_ directory for both servers to call any external Weather server with open API (I propose to use [this one](https://open-meteo.com/)).
    - Add endpoint _/weather_ for both servers and use a single common code without duplication.
    - Parse all incoming data with `Pydantic` models and handle it in console somewhere.

### Additional Challenges (For both servers):
1. **Middleware:**
    - Implement a middleware that adds a custom header to every response.

2. **Error Handling:**
    - Implement error handling for common HTTP errors (e.g., 404 Not Found, 500 Internal Server Error).

3. **Dockerization (Optional):**
    - Create a Dockerfile for each server to containerize both the sync and async applications.

4. **Tests:**
    - Write unit tests using `pytest` for the main functionality of both the sync and async servers.

5. **Stress-test**
     - Add in each server several endpoints to simulate I/O & CPU bound tasks and something else to simulate error on server-side e.g. _/io_task_, _/cpu_task_, _/error_task_, etc.
     - Install `locust` package in your local env and write a script to stress-test two servers.
     - It would be cool to plot a graph on the data obtained from locust and put it in the documentation.


### Submission:
- All Python code **MUST** be _typed_ (the `typing` module to your rescue).
- Implement the project according to the `PEP8` standard should be described in the `tool` section of the _pyproject.toml_ for linters with some modifications:
    + String length should be 120 characters.
    + Count of lines after import should be 2.
    + The rest is by specification.
- `Pytest` configs also should be in in the `tool` section of the _pyproject.toml_.
- Commit style, [click](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/). Commits should contain small logical portions of the code being modified. A clear commit name is required, descriptions within commits are welcome. The commit header should be up to 50 characters and the description up to 72 characters, [read more](https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting).
- Branch style, [click](https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf#:~:text=own%20development%20cycle.-,Git%20Flow,-The%20Git%20Flow). It is suggested to use GitFlow. Don't forget to delete merged or close branches based on PR status. Development should be done in separate branches, it is not allowed to commit or merge changes directly into _master_ or _develop_.
- Commits, branches and PR's should contain small pieces of separate logic so that it can be revisited. There is EXAMPLE, how to decompose and get started (documentation should also be also updated):
  + The first PR would be enough to see poetry installed and a project structure.
  + The second PR sync server.
  + The third PR async server.
  + The fourth PR Docker.
  + The fifth PR external API call.
- Try to follow all [OOP](https://realpython.com/python3-object-oriented-programming/) & [design](https://www.boldare.com/blog/kiss-yagni-dry-principles/) principles.
- Submit the codebase along with a detailed README explaining how to set up and run the monolithic application, any additional features implemented, and any challenges faced. [Here is](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) a good cheat-list how to style documentation.
- Fork this repository and do your development there.


### Note:
- Use Python 3.10 or above.
- Feel free to use any additional libraries or tools you find suitable for the task.
- Try decomposing tasks into chunks and branches as described above.
- All `highlighted` words should be read in the documentation or familiarized with what they are.
- Follow best practices in terms of code readability, structure, and documentation.


### Suggested project structure:
```
./
├── src/
│   ├── app/
│   │   ├── async/
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── sync/
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   └── __init__.py
│   ├── core/
│   │   └── __init__.py
│   └── __init__.py
├── README.md
└── task.md
```
