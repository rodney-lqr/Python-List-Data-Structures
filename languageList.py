languageList = ["English", "Spanish", "Chinese", "Hindi", "Arabic", "Portuguese", "Bengali", "Russian", "Japanese", "Punjabi", "Marathi", "Telugu", "German", "French", "Javanese", "Urdu", "Vietnamese", "Korean", "Turkish", "Italian"]


print("Entire list:", languageList)
print("The 13th index is: ", languageList[12])
print()
languageList[9] = "Spanish"
del languageList[15]

for x in languageList:
    print(x)
print()
print(languageList[6:11])
print()
print("The last index: is", languageList[-1])
print()