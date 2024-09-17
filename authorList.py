authors = ["William Shakespeare", "Jane Austen", 
    "Charles Dickens", "Sara Tambaloslos", 
    "Leo Tolstoy", "F. Scott Fitzgerald", 
    "Ernest Hemingway", "George Orwell", 
    "Harper Lee", "J.R.R. Tolkien", 
    "Gabriel García Márquez", "J.K. Rowling"
]

print()
print(authors)
print()
print("The 6th index is: ", authors[6])
print()
authors[4] = "Mark Twain"
authors.remove(authors[10])
for x in authors:
    print(x)

print()
print(authors[3:8])
print()
print("The last index is: ", authors[-1])
print()
