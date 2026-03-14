import xml.etree.ElementTree as ET
import glob
import json

results = []

def mine_selectors(path):
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        tree = ET.parse(file)
        for elem in tree.iter():
            res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
            if res_id:
                results.append({
                    "file": file.split("\\")[-1],
                    "id": res_id.split("/")[-1],
                    "tag": elem.tag
                })

mine_selectors("../Artefakt02/decompiledapk/res/layout")

with open("miner_report.json", "w") as f:
    json.dump(results, f, indent=4)

print("Report generated: miner_report.json")