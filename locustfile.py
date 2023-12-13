from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def hello(self):
        self.client.get("/hello")

    @task
    def io_task(self):
        self.client.get("/io_task")

    @task
    def cpu_task(self):
        self.client.get("/cpu_task")

    @task
    def random_sleep(self):
        self.client.get("/random_sleep")

    @task
    def random_status(self):
        self.client.get("/random_status")

    @task
    def chain(self):
        self.client.get("/chain")

    @task
    def error_test(self):
        self.client.get("/error_test")
