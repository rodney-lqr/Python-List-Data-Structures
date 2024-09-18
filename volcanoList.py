famousVolcanoes = [
    "Mount Fuji (Japan)",
    "Mount Kilimanjaro (Tanzania)",
    "Mount Pinatubo (Philippines)",
    "Mount Etna (Italy)",
    "Mount Saint Helens (United States)",
    "Mauna Loa (Hawaii, United States)",
    "Mount Krakatoa (Indonesia)"
]

print()
print(famousVolcanoes)
print()
print("The 4th index is: ", famousVolcanoes[3])
print()
famousVolcanoes[2] = "Mount Vesuvius (Italy)"
del famousVolcanoes[4]
for x in famousVolcanoes:
    print(x)

print()
print("The last index is: ", famousVolcanoes[-1])
print()