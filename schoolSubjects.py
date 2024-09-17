schoolSubjects = [
    "English",
    "Science",
    "History",
    "Geography",
    "Art",
    "Music",
    "Physical Education",
    "Computer Science",
    "Home Economics",
    "Philosophy",
    "Psychology",
    "Sociology"
]

print()
print(schoolSubjects)
print()
print("The 6th index is: ", schoolSubjects[5])
print()
schoolSubjects[7] = "Mathematics"
del schoolSubjects[4]
for x in schoolSubjects:
    print(x)
print()
print(schoolSubjects[1:4])
print() 
print("The last index is: ", schoolSubjects[-1])
print()