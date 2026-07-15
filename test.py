import requests

url = "http://127.0.0.1:5000/calculate"

data = {
    "math": 80,
    "science": 90,
    "history": 70
}

response = requests.post(url, json=data)

print(response.json())