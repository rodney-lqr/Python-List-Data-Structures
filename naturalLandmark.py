naturalLandmarks = [
    "Niagara Falls",
    "Great Barrier Reef",
    "Mount Everest",
    "Victoria Falls",
    "Iguazu Falls",
    "Galapagos Islands",
    "Amazon Rainforest",
    "Yellowstone National Park",
    "Uluru (Ayers Rock)",
    "Salar de Uyuni"
]

print()
print(naturalLandmarks)
print()
print("The 8th index is: ", naturalLandmarks[7])
print()
naturalLandmarks[4] = "Grand Canyon"
del naturalLandmarks[8]
for x in naturalLandmarks:
    print(x)

print()
print("The last index is: ", naturalLandmarks[-1])
print()