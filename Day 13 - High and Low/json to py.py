import json
import pprint

with open(r"db.json", "r", encoding="utf-8") as file:
    data = json.load(file)

objects = data["objects"]

with open("db.py", "w", encoding="utf-8") as file:
    file.write("objects = ")
    file.write(pprint.pformat(objects, width=120))
    file.write("\n")