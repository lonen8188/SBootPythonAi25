import requests

url = "http://127.0.0.1:8000/detect" # 요청보낼 url
message = "Test message"             # 서버로 전송할 메시지(폼 데이터로 전송)
file_path = "test.jpg"             # 전송할 이미지 파일 경로(py와 같은 경로에 존재)

with open(file_path, "rb") as file: # rb는 읽기모드(바이너리)
    response = requests.post(url, data={"message": message},
                             files={"file": file})


print(response.json())