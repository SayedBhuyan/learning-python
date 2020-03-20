def add(*details):
    sum = 0
    for val in details:
        sum = sum + val
    return sum


print(add(10, 20))