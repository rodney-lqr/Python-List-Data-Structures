currencies = [
    "US Dollar",
    "British Pound",
    "Japanese Yen",
    "Chinese Yuan",
    "Indian Rupee",
    "Canadian Dollar",
    "Australian Dollar",
    "South African Rand",
    "Brazilian Real",
    "Russian Ruble"
]

print()
print(currencies)
print()
print("The 4th index is: ", currencies[3])
currencies[6] = "Euro"
del currencies[8]
for x in currencies:
    print(x)

print()
print("The last index is: ", currencies[-1])
print()