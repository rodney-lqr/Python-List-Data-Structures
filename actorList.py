famousActors = [
    "Tom Hanks",
    "Meryl Streep",
    "Brad Pitt",
    "Scarlett Johansson",
    "Robert Downey Jr.",
    "Nicole Kidman",
    "Denzel Washington",
    "Natalie Portman",
    "Will Smith",
    "Julia Roberts"
]

print()
print(famousActors)
print()
print("The 7th index is: ", famousActors[6])
print()
famousActors[2] = "Leonardo Di Caprio"
del famousActors[7]
for x in famousActors:
    print(x)

print()
print("The last index is: ", famousActors[-1])
print()
