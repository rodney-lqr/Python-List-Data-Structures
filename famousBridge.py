famousBridges = [
    "Tower Bridge",
    "Sydney Harbour Bridge",
    "Akashi Kaikyō Bridge",
    "Ponte Vecchio",
    "Charles Bridge",
    "Boro Bridge",
    "Brooklyn Bridge",
    "Millennium Bridge"
]

print()
print(famousBridges)
print()
print("The 3rd index is: ", famousBridges[2])
print()
famousBridges[5] = "Golden Gate Bridge"
del famousBridges[6]
for x in famousBridges:
    print(x)

print()
print("The last index is: ", famousBridges[-1])
print()