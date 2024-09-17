holidays = [
    "Lunar New Year",
    "New Year's Day",
    "Valentine's Day",
    "Easter",
    "Mother's Day",
    "Father's Day",
    "Independence Day",
    "Halloween",
    "Thanksgiving",
    "Hanukkah",
    "Ramadan",
    "Eid al-Fitr"
]

print()
print(holidays)
print()
print("The 9th index is: ", holidays[8])
holidays[2] = "Christmas"
del holidays[10]
for x in holidays:
    print(x)

print()
print(holidays[1:6])
print()
print(holidays[-1])
print()
