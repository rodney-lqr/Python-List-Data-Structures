oceans = [
    "Atlantic Ocean",
    "Indian Ocean",
    "Arctic Ocean",
    "Southern Ocean",
    "Mediterranean Sea"
]

print()
print(oceans)
print()
print("The 3rd index is: ", oceans[2])
print()
oceans[1] = "Pacific Ocean"
del oceans[3]
for x in oceans:
    print(x)

print()
print("The last index is: ", oceans[-1])
print()