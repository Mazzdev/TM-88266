import json
import xml.etree.ElementTree as ET

score = 100
deductions = []

# 8.1 permissions + debuggable
try:
    tree = ET.parse("RiskyPermission.xml")
    root = tree.getroot()

    risky_permissions = root.findall("permission")
    for perm in risky_permissions:
        score -= 5
        deductions.append(f"LOW: Ryzykowne uprawnienie {perm.get('name')} (-5)")

    debuggable = root.find("debuggable")
    if debuggable is not None and debuggable.text == "true":
        score -= 30
        deductions.append("HIGH: Debuggable=true (-30)")
except Exception as e:
    deductions.append(f"ERROR: Nie udało się odczytać RiskyPermission.xml: {e}")

# 8.3 vulnerabilities
try:
    with open("83_vulnerabilities.json", "r", encoding="utf-8") as f:
        vulns = json.load(f)

    for vuln in vulns:
        severity = vuln.get("severity")

        if severity == "CRITICAL":
            score -= 50
            deductions.append(f"CRITICAL: {vuln.get('library')} (-50)")
        elif severity == "HIGH":
            score -= 30
            deductions.append(f"HIGH: {vuln.get('library')} (-30)")
        elif severity == "MEDIUM":
            score -= 15
            deductions.append(f"MEDIUM: {vuln.get('library')} (-15)")
        elif severity == "LOW":
            score -= 5
            deductions.append(f"LOW: {vuln.get('library')} (-5)")
except Exception as e:
    deductions.append(f"ERROR: Nie udało się odczytać 83_vulnerabilities.json: {e}")

if score < 0:
    score = 0

status = "APPROVED" if score >= 80 else "NEEDS FIX" if score >= 50 else "REJECTED"

report = []
report.append(">>> ZADANIE 8.4: SECURITY SCORE <<<")
report.append(f"WYNIK KOŃCOWY: {score}/100")
report.append(f"STATUS: {status}")
report.append("")
report.append("Potrącenia punktów:")

for item in deductions:
    report.append(f"- {item}")

with open("84_risk_score.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("\n".join(report))
print("Zapisano: 84_risk_score.txt")