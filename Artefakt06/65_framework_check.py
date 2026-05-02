import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime

from BasePage import BasePage
from MainPage import MainPage

results = []

# 1. Czy MainPage dziedziczy po BasePage?
if issubclass(MainPage, BasePage):
    results.append(("POM inheritance", "PASSED"))
else:
    results.append(("POM inheritance", "FAILED"))

# 2. Czy raport audytu istnieje i jest Markdown?
if os.path.exists("64_audit_report.md") and "RAPORT AUDYTU" in open("64_audit_report.md", encoding="utf-8").read():
    results.append(("Markdown audit report", "PASSED"))
else:
    results.append(("Markdown audit report", "FAILED"))

# 3. Czy selektory istnieją?
try:
    with open("../Artefakt05/53_selectors.json", "r", encoding="utf-8") as f:
        selectors = json.load(f)

    if len(selectors) > 0:
        results.append(("Selector map", "PASSED"))
    else:
        results.append(("Selector map", "FAILED"))
except Exception:
    results.append(("Selector map", "FAILED"))

testsuite = ET.Element("testsuite")
testsuite.set("name", "FrameworkIntegrityTest")
testsuite.set("tests", str(len(results)))
testsuite.set("failures", str(sum(1 for _, status in results if status == "FAILED")))
testsuite.set("timestamp", datetime.now().isoformat())

for name, status in results:
    testcase = ET.SubElement(testsuite, "testcase")
    testcase.set("name", name)
    testcase.set("status", status)

    if status == "FAILED":
        failure = ET.SubElement(testcase, "failure")
        failure.set("message", f"{name} failed")

tree = ET.ElementTree(testsuite)
tree.write("65_final_report.xml", encoding="utf-8", xml_declaration=True)

print(">>> WYNIK AUDYTU FRAMEWORKA <<<")
for name, status in results:
    print(f"{name}: {status}")

print("Zapisano raport: 65_final_report.xml")