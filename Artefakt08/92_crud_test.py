import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "test",
    "body": "api test",
    "userId": 1
}

print(">>> ZADANIE 9.2: CRUD <<<")

response = requests.post(url, json=data)

print(f"STATUS: {response.status_code}")

if response.status_code == 201:
    print("[SUCCESS] Zasób stworzony pomyślnie!")
    print(response.json())
else:
    print("[ERROR] Nie udało się utworzyć zasobu")