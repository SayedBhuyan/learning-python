books = []

books.append("C")
books.append("C++")
books.append("Python")
books.append("Javascript")

print(books)

books.pop()
print(books)
print("Now the top book is: ", books[-1])


books.pop()
print(books)
print("Now the top book is: ", books[-1])


books.pop()
print(books)
print("Now the top book is: ", books[-1])


books.pop()
print(books)

if not books:
    print("No books left")