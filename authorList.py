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
print("The 6th index is: ", authors[5])
print()
authors[3] = "Mark Twain"
authors.remove(authors[9])
for x in authors:
    print(x)

print()
print(authors[3:8])
print()
print("The last index is: ", authors[-1])
print()
