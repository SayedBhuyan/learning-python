def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def large(a, b):
    if a > b:
        return a
    else:
        return b


def avg(a, b):
    return (a + b) / 2


x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))

result = add(x, y)
print("Sub:", result)

result = sub(x, y)
print("Sum:", result)

result = large(x, y)
print("Large:", result)

result = avg(x, y)
print("Large:", result)

maximum = large
print(maximum(2,3))



