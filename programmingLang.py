programmingLanguages = [
    'Cobol','JavaScript',
    'Java','C++',
    'C#','Ruby',
    'Go','Swift',
    'Kotlin','TypeScript',
    'PHP','Rust',
    'Perl','R',
    'Dart'
]

print()
print(programmingLanguages)
print()
print("The 11th index is: ", programmingLanguages[10])
print()
programmingLanguages[8] = "Python"
programmingLanguages.remove(programmingLanguages[12])
print()
for x in programmingLanguages:
    print(x)

print()
print(programmingLanguages[5:12])
print()
print("The last index is: ", programmingLanguages[-1])
print()