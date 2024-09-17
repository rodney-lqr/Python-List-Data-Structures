famousInventions = [
    "Transistor",
    "Telephone",
    "Airplane",
    "Computer",
    "Internet",
    "Smartphone",
    "Penicillin",
    "Wheel"
]

print()
print(famousInventions)
print()
print("The 6th index is: ", famousInventions[5])
print()
famousInventions[1] = "Lightbulb"
del famousInventions[4]
for x in famousInventions:
    print(x)

print()
print("The last index is: ", famousInventions[-1])
print()