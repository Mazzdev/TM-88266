import xml.etree.ElementTree as ET
import glob
import json

gaps = []

for file in glob.glob("../Artefakt02/decompiledapk/res/layout/**/*.xml", recursive=True):
    tree = ET.parse(file)

    for elem in tree.iter():
        text = elem.get('{http://schemas.android.com/apk/res/android}text')
        desc = elem.get('{http://schemas.android.com/apk/res/android}contentDescription')

        if text and not desc:
            gaps.append({
                "file": file.split("\\")[-1],
                "text": text,
                "issue": "Missing contentDescription"
            })

with open("a11y_report.json", "w") as f:
    json.dump(gaps, f, indent=4)

print("A11y report generated")