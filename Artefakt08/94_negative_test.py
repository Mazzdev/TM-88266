import requests

url = "https://jsonplaceholder.typicode.com/posts/9999"

print(">>> ZADANIE 9.4: NEGATIVE TEST <<<")

response = requests.get(url)

print(f"STATUS: {response.status_code}")

if response.status_code == 404:
    print("[SUCCESS] API poprawnie zwróciło 404 Not Found")
else:
    print("[ERROR] Niepoprawna obsługa błędu")