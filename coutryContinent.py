countriesAndContinents = [
    ("United States", "North America"),
    ("Canada", "North America"),
    ("Mexico", "North America"),
    ("Brazil", "South America"),
    ("Argentina", "South America"),
    ("China", "Asia"),
    ("India", "Asia"),
    ("Japan", "Asia"),
    ("New Zealand", "Oceania"),
    ("Russia", "Europe"),
    ("France", "Europe"),
    ("Germany", "Europe"),
    ("Egypt", "Africa"),
    ("South Africa", "Africa")
]

print()
print(countriesAndContinents)
print()
print("The 9th index is: ", countriesAndContinents[8])
countriesAndContinents[9] = "Australia"
del countriesAndContinents[11]
for x in countriesAndContinents:
    print(x)

print()
print(countriesAndContinents[3:7])
print()
print("The last index is: ", countriesAndContinents[-1])
print()