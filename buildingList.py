famousBuildings = [
    "The Colosseum",
    "The Taj Mahal",
    "The Great Wall of China",
    "The Burj Khalifa",
    "The Empire State Building",
    "The Sydney Opera House",
    "The Sagrada Família",
    "The Petronas Towers"
]

print()
print(famousBuildings)
print()
print("The 5th index is: ", famousBuildings[4])
print()
famousBuildings[1] = "Eiffel Tower"
del famousBuildings[5]
for x in famousBuildings:
    print(x)
print()
print("The last index is: ", famousBuildings[-1])
print()
