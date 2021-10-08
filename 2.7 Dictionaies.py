"""
DICTIONAIRS

- Concept
    - Like a list
    - Instead of indicies, you have keys.
- Creating a dictionary
    - Empty
    - With starting values
        - Key/value pairs
- Adding a value
- Modifying a value
- Removing a value
- Iterating through a dictionary keys
- Iterating through a dictionary values
- Iterating through a dictionary keys and values
"""

player = [100, "Frankie", "Wizzard"]
#                                                  dictionairs help store this info better

print(f"The player's health is: {player[0]}")

#-----------------------------

player = {}   # emty dictionairy

# 0 - health
# 1 - name
# 2 - class

player = {
    # key : value
    "health": 100,
    "name": "Frankie",
    "class": "Wizzard",
    0: "why would you?",
    2.1: "level up",
    1: "why?"
}

print(f"Player health is {player['health']}")

player["strength"] = 50        # adds strength to player dictionairy
print(player["strength"])

player["health"] = 90         # replaces player health to 90
print(player["health"])

print(player[0])             # prints "why would you"

print(player[2.1])             # prints "level up"

print(player[1])
del player[1]                  # deletes key [1] "why?"
 
for key in player.keys():
    print(key)                 # prints all the keys in the dictionairy

for value in player.values():
    print(value)              # prints all the values in the dictionairy


#[("health", 100), ("name," "Frankie")]
for key, value in player.items():
    print(key, value)                     # prints both key and value
