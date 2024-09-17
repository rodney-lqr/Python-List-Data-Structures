Tools = [
    "Tape Measure",
    "Saw",
    "Level",
    "Screwdriver",
    "Chisel",
    "Plane",
    "Clamps",
    "Drill",
    "Router",
    "Utility Knife"
]

print()
print(Tools)
print()
print("The 4th index is: ", Tools[3])
print()
Tools[6] = "Hammer"
print()
del Tools[4]
for x in Tools:
    print(x)

print()
print(Tools[-1])
print()
