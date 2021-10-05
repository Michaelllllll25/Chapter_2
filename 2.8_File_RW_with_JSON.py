# Write JSON data to a file
# JavaScript Object Notation 
import json

data = {
    "name": "Jeff",
    "marks": [77, 88, 99],      # save this dictionair int a file
    "happy": True
}

with open("jeff_info.json", "w") as f:
    json.dump(data, f, indent=4)         # indent makes it nicer

# Load JSON data from a file
with open("jeff_info.json", "r") as f:
    data = json.load(f)
#                                           save it, doesnt change in the file
data["happy"] = False
print(data)

# need to re-write the data to change it in the file
with open("jeff_info.json", "w") as f:
    json.dump(data, f, indent=4)              # changes the file
