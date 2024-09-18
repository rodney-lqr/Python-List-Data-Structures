recipes = [
    "Spaghetti Bolognese",
    "Chicken Alfredo",
    "Beef Stroganoff",
    "Sushi",
    "Pizza",
    "Tacos",
    "Burritos",
    "Quesadillas",
    "Pad Thai",
    "Ramen",
    "Curry",
    "Chili",
    "Mac and Cheese",
    "Chicken Pot Pie",
    "Shepherd's Pie"
]

print()
print(recipes)
print()
print("The 12th index is: ", recipes[11])
recipes[8] = "Lasagna"
del recipes[10]
for x in recipes:
    print(x)

print()
print(recipes[4:9])
print()
print("The last index is: ", recipes[-1])
print()