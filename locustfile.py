from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def hello(self) -> None:
        self.client.get("/hello")

    @task
    def io_task(self) -> None:
        self.client.get("/io_task")

    @task
    def cpu_task(self) -> None:
        self.client.get("/cpu_task")

    @task
    def random_sleep(self) -> None:
        self.client.get("/random_sleep")

    @task
    def random_status(self) -> None:
        self.client.get("/random_status")

    @task
    def chain(self) -> None:
        self.client.get("/chain")

    @task
    def error_test(self) -> None:
        self.client.get("/error_test")
