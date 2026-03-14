import json
from collections import Counter

with open("miner_report.json") as f:
    data = json.load(f)

tags = [item["tag"] for item in data]
total = len(tags)

counter = Counter(tags)

report = {
    "metrics": {},
    "verdict": "LOW RISK"
}

for tag, count in counter.items():
    percent = (count / total) * 100
    report["metrics"][tag] = f"{percent:.2f}%"

    if percent > 50:
        report["verdict"] = "HIGH RISK"

with open("stability_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Audit complete:", report["verdict"])