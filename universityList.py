universities = [
    "Stanford University",
    "Massachusetts Institute of Technology (MIT)",
    "Yale University",
    "Princeton University",
    "Columbia University",
    "University of California, Berkeley",
    "University of Chicago",
    "University of Pennsylvania",
    "Duke University",
    "Johns Hopkins University"
]

print()
print(universities)
print()
print("The 6th index is: ", universities[5])
print()
universities[3] = "Harvard University"
del universities[8]
for x in universities:
    print(x)

print()
print("The last index is: ", universities[-1])
print()