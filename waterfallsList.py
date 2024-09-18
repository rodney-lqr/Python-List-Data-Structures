famousWaterfalls = [
    "Victoria Falls",
    "Angel Falls",
    "Iguazu Falls",
    "Yosemite Falls",
    "Kaieteur Falls",
    "Dettifoss",
    "Plitvice Lakes",
    "Tugela Falls",
    "Ban Gioc-Detian Falls",
    "Skógafoss"
]

print()
print(famousWaterfalls)
print()
print("The 8th index is: ", famousWaterfalls[7])
print()
famousWaterfalls[4] = "Niagra Falls"
del famousWaterfalls[8]
for x in famousWaterfalls:
    print(x)

print()
print("The last index is: ", famousWaterfalls[-1])
print()