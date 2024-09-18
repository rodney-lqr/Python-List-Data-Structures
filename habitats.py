animalHabitats = [
    "Rainforest",
    "Desert",
    "Tundra",
    "Taiga",
    "Grassland",
    "Ocean",
    "Arctic",
    "Freshwater"
]

print()
print(animalHabitats)
print()
print("The 5th index is: ", animalHabitats[4])
print()
animalHabitats[2] = "Savannah"
del animalHabitats[5]
for x in animalHabitats:
    print(x)

print()
print("The last index is: ", animalHabitats[-1])
print()


