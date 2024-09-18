drinks = [
    "Tea",
    "Soda",
    "Juice",
    "Milk",
    "Water",
    "Wine",
    "Beer",
    "Cocktail"
]

print()
print(drinks)
print()
print("The 4th index is: ", drinks[3])
print()
drinks[2] = "Coffee"
del drinks[6]
for x in drinks:
    print(x)

print()
print("The last index is: ", drinks[-1])
print()
