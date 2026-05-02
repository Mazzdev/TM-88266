import os
import re

BASE_DIR = "../Artefakt02/decompiledapk"
OUTPUT_TXT = "82_secrets_found.txt"

patterns = {
    "URL": r"https?://[^\s\"'>]+",
    "IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "API_KEY": r"(?i)(api[_-]?key|apikey|secret|token|password|passwd|firebase|google)",
}

findings = []

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith((".xml", ".txt", ".json", ".properties", ".gradle", ".smali")):
            path = os.path.join(root, file)

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                for label, pattern in patterns.items():
                    matches = re.findall(pattern, content)

                    for match in matches:
                        findings.append(f"[{label}] {path} -> {match}")

            except Exception:
                continue

with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
    if findings:
        f.write("\n".join(findings))
    else:
        f.write("Brak potencjalnych sekretów.\n")

print(">>> ZADANIE 8.2: HARDCORED SECRETS SCANNER <<<")
print(f"Znaleziono potencjalne sekrety: {len(findings)}")
print(f"Zapisano: {OUTPUT_TXT}")

for item in findings[:10]:
    print(item)