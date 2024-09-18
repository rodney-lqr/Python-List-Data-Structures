worldWonders = [
    "Chichen Itza",
    "Petra",
    "Machu Picchu",
    "Christ the Redeemer",
    "Colosseum",
    "Taj Mahal",
    "Christ the Redeemer"
]

print()
print(worldWonders)
print()
print("The 4th index is: ", worldWonders[3])
print()
worldWonders[1] = "Great Wall of China"
del worldWonders[4]
for x in worldWonders:
    print(x)

print()
print("The last index is: ", worldWonders[-1])
print()

