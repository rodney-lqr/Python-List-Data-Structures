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
print("The 11th index is: ", programmingLanguages[11])
print()
programmingLanguages[9] = "Python"
programmingLanguages.remove(programmingLanguages[13])
print()
for x in programmingLanguages:
    print(x)

print()
print(programmingLanguages[5:12])
print()
print("The last index is: ", programmingLanguages[-1])
print()