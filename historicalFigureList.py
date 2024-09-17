historicalFigures = [
    "Alexander the Great",
    "Julius Caesar",
    "Queen Elizabeth I",
    "Napoleon Bonaparte",
    "Abraham Lincoln",
    "Albert Einstein",
    "Marie Curie",
    "Martin Luther King Jr.",
    "Winston Churchill",
    "Malala Yousafzai"
]

print()
print(historicalFigures)
print()
print("The 6th index is: ", historicalFigures[7])
print()
historicalFigures[3] = "Nelson Mandela"
del historicalFigures[6]
for x in historicalFigures:
    print(x)

print("The last index is: ", historicalFigures[-1])
print()
