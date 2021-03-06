# File R/W
# --------

### Read from a file      r means read f means file
with open("some_file.txt", "r") as f:
    contents = f.read()
    
print(contents)

### Read multiple lines
with open("read_multiple_lines.txt", "r") as f:    # r means read
    for line in f:
        print(line.strip())      # removes spaces (.strip())

### Write to a file
with open("write_to_file.txt", "w") as f:          # w means write
    f.write("Hello. I am writing to a file!\n")    # \n puts it on next line  
    f.write("Next Line!")

### Append to a file
with open("append_to_file.txt", "a") as f:   # a mean append (means don't override, just add it to the end)
    f.write("hello")

### Write multiple lines from a file
marks = [56, 87, 34, 76, 87, 88]

with open("marks.txt", "w") as f:
    for mark in marks:
        f.write(f"{mark}, ")        #have to convert int to str because files only take strings

### Write JSON data to a file
# JSON- JavaScript Object Notation (send and recieve data over the web)
import json     # imports should be at the top of the code

data = {
    "name": "Jeff",
    "marks": [77, 88, 99],
    "happy": True
}

with open("jeff_info.json", "w") as f:
    json.dump(data, f, indent=4)

### Load JSON data from a file

with open("jeff_info.json", "r") as f:
    data = json.load(f)

data["happy"] = False

# need to re-write the data to change it in the file
with open("jeff_info.json", "w") as f:    # change the true to false
    json.dump(data, f, indent=4)          #   ^

with open("append_to_file.txt", "w") as f:               
    f.write()                                         # Overwrites and entire document to be blank
