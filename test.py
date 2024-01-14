from data import *

with open("test.json") as data_file:
    raw_data = data_file.read()
data = json.loads(raw_data)

try:
    data["test"]["1"] += 1
except KeyError:
    data["test"]["1"] = 1

raw_data = json.dumps(data, indent=4)
with open("test.json", "w") as data_file:
    data_file.write(raw_data)