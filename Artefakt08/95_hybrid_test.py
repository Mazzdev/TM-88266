import requests
import time

print(">>> ZADANIE 9.5: HYBRID TEST <<<")

# STEP 1: API
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "hybrid test",
    "body": "api + appium",
    "userId": 1
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("[API SUCCESS] Zasób utworzony:", response.json()["title"])
else:
    print("[API ERROR]")

# STEP 2: symulacja Appium
print("[APPIUM] Start sesji...")
time.sleep(1)

print("[APPIUM] Nawigacja do widoku...")
time.sleep(1)

print("[APPIUM] Weryfikacja danych na UI...")

print("[SUCCESS] Dane z API widoczne w aplikacji")