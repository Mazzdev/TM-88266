import xml.etree.ElementTree as ET

MANIFEST = "../Artefakt02/decompiledapk/AndroidManifest.xml"
ANDROID_NS = "{http://schemas.android.com/apk/res/android}"

dangerous = [
    "READ_SMS", "SEND_SMS", "RECEIVE_SMS",
    "READ_CONTACTS", "WRITE_CONTACTS",
    "ACCESS_FINE_LOCATION", "ACCESS_COARSE_LOCATION",
    "RECORD_AUDIO", "CAMERA", "READ_PHONE_STATE"
]

tree = ET.parse(MANIFEST)
root = tree.getroot()

report = ET.Element("RiskyPermissions")
found = 0

for perm in root.findall("uses-permission"):
    name = perm.attrib.get(ANDROID_NS + "name", "")
    short = name.split(".")[-1]

    if short in dangerous:
        item = ET.SubElement(report, "permission")
        item.set("name", name)
        item.set("risk", "HIGH")
        found += 1

application = root.find("application")
debuggable = application.attrib.get(ANDROID_NS + "debuggable", "false") if application is not None else "false"

debug = ET.SubElement(report, "debuggable")
debug.text = debuggable
debug.set("risk", "HIGH" if debuggable == "true" else "LOW")

ET.ElementTree(report).write("RiskyPermission.xml", encoding="utf-8", xml_declaration=True)

print(">>> ZADANIE 8.1: AUDYT UPRAWNIEŃ <<<")
print(f"Znaleziono ryzykowne uprawnienia: {found}")
print(f"Debuggable: {debuggable}")
print("Zapisano: RiskyPermission.xml")