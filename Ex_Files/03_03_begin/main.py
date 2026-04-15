import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}


# converting from a Python Dictionary to a JSON using json.dumps()
einstein_json = json.dumps(EINSTEIN)

# converting JSON back to dictionary using json.loads()
back_to_dict = json.loads(einstein_json)


print(einstein_json)
pprint(back_to_dict)


# read from laureates.csv to converting data to a list
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# use laureates variable to create and write a file called laureates.json
# to write in
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
