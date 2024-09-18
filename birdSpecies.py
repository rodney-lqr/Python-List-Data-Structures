birdSpecies = [
    "Robin",
    "Sparrow",
    "Pigeon",
    "Crow",
    "Hummingbird",
    "Owl",
    "Parrot",
    "Peacock",
    "Flamingo",
    "Penguin",
    "Duck",
    "Goose"
]

print()
print(birdSpecies)
print()
print("The 9th index is: ", birdSpecies[8])
print()
birdSpecies[5] = "Eagle"
del birdSpecies[7]
for x in birdSpecies:
    print(x)

print()
print(birdSpecies[2:6])
print()
print("The last index is: ", birdSpecies[-1])
print()