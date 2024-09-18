spaceMissions = [
    "Voyager 1",
    "Voyager 2",
    "Cassini-Huygens",
    "Galileo",
    "Juno",
    "Curiosity",
    "Opportunity",
    "Mars Pathfinder",
    "Hubble Space Telescope",
    "James Webb Space Telescope"
]

print()
print(spaceMissions)
print()
print("The 5th index is: ", spaceMissions[6])
print()
spaceMissions[3] = "Apollo 11"
del spaceMissions[5]
for x in spaceMissions:
    print(x)

print()
print("The last index is: ", spaceMissions[-1])
print()