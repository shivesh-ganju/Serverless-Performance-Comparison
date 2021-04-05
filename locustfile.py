from locust import HttpUser, task, between,constant
from json import JSONDecodeError

class MyUser(HttpUser):
    wait_time = constant(1)
    host='https://8ejhh12fx6.execute-api.us-east-1.amazonaws.com/beta/inception-method'
    @task(1)
    def index(self):
        with self.client.get("/", catch_response=True) as response:
            print(response.text)