import requests
from jsonschema import validate

url = "https://jsonplaceholder.typicode.com/posts/1"

schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

print(">>> ZADANIE 9.3: SCHEMA VALIDATION <<<")

response = requests.get(url)
data = response.json()

validate(instance=data, schema=schema)

print("[SUCCESS] Struktura JSON poprawna")