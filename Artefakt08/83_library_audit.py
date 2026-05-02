import json

vulnerability_db = {
    "com.google.android.gms:10.0.1": {
        "severity": "HIGH",
        "cve": "CVE-2016-XXXX",
        "description": "Stara wersja Google Play Services"
    },
    "com.squareup.okhttp:2.7.5": {
        "severity": "CRITICAL",
        "cve": "CVE-2021-0341",
        "description": "Podatna wersja biblioteki HTTP"
    },
    "org.apache.commons:1.0.0": {
        "severity": "CRITICAL",
        "cve": "CVE-2019-XXXX",
        "description": "Ryzyko zdalnego wykonania kodu"
    },
    "com.android.support:25.0.0": {
        "severity": "MEDIUM",
        "cve": "CVE-2017-XXXX",
        "description": "Stara biblioteka wsparcia Android"
    }
}

with open("requirements.txt", "r", encoding="utf-8") as f:
    libraries = [line.strip() for line in f if line.strip() and not line.startswith("#")]

results = []

print(">>> ZADANIE 8.3: ANALIZA PODATNOŚCI BIBLIOTEK <<<")

for lib in libraries:
    vuln = vulnerability_db.get(lib)

    if vuln:
        item = {
            "library": lib,
            "severity": vuln["severity"],
            "cve": vuln["cve"],
            "description": vuln["description"]
        }
        results.append(item)

        print(f"[{vuln['severity']}] {lib} -> {vuln['cve']}")
    else:
        print(f"[OK] {lib} - brak znanej podatności")

with open("83_vulnerabilities.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print(f"Zapisano: 83_vulnerabilities.json")
print(f"Wykryto podatności: {len(results)}")