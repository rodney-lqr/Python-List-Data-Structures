continents = [
    "Asia",
    "Africa",
    "North America",
    "South America",
    "Europe",
    "Oceania",
    "Antarctica"
]

print()
print(continents)
print()
print("The 4th index is: ", continents[3])
print()
continents[1] = "Africa"
del continents[5]
for x in continents:
    print(x)

print()
print(continents[-1])
print()