import json

with open("miner_report.json") as f:
    data = json.load(f)

target_id = input("Enter id: ")
target_tag = input("Enter tag: ")

matches = [x for x in data if x["id"] == target_id and x["tag"] == target_tag]

if len(matches) == 1:
    print("STATUS: ZALICZONE! Twój selektor jest unikalny.")
else:
    print("Selector not unique")