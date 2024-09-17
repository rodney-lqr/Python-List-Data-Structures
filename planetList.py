planetList = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus","Neptune",]

print()
print(planetList)
print()
print("The 3rd index is: ", planetList[2])
print()
planetList[6] = "Pluto"
planetList.remove(planetList[3])

for x in planetList:
    print(x)

print()
print("This is the last index: ", planetList[-1])
print()