festivals = [
    "Christmas",
    "New Year's Eve",
    "Halloween",
    "Easter",
    "Eid al-Fitr",
    "Diwali",
    "Hanukkah",
    "Chinese New Year",
    "Valentine's Day",
    "Cinco de Mayo"
]

print()
print(festivals)
print()
print("The 5th index is: ", festivals[4])
festivals[2] = "Thanksgiving"
del festivals[6]
for x in festivals:
    print(x)

print()
print("The last index is: ", festivals[-1])
print()