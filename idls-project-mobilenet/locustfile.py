from locust import HttpUser, task, between,constant
from json import JSONDecodeError
import json

class MyUser(HttpUser):
    wait_time = constant(1)
    host='https://e9dtxz5ep9.execute-api.us-east-1.amazonaws.com/beta/mobilenet'
    @task(1)
    def index(self):
        file = open('results_4096.txt','a')
        with self.client.get("/", catch_response=True) as response:
            print(response)
            print(json.loads(response.text)['body'][1:-1])
            file.write(json.loads(response.text)['body'][1:-1])
            file.write('\n')
            file.close()