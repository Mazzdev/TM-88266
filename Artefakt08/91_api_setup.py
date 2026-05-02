import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

print(">>> ZADANIE 9.1: API SETUP <<<")

response = requests.get(url)

print(f"STATUS: {response.status_code}")

if response.status_code == 200:
    print("[SUCCESS] API jest dostępne")
    print("Response:", response.json())
else:
    print("[ERROR] API niedostępne")