from locust import HttpUser, task, between

class User(HttpUser):
    
    @task
    def predict_iris(self):
        wait_time = between(1, 2)

        # Get 요청을 보냅니다.
        response = self.client.get("/movies/ott/")

        # 응답 확인 (예: 상태 코드, JSON 응답 등)
        if response.status_code == 200:
            print("Success")
        else:
            print("Failed")

    def on_start(self):
        print("START LOCUST")

    def on_stop(self):
        print("STOP LOCUST")

