numbers = [1, 2, 3, 4, 5, 6,7,8,9]

def mapper(x):
    return x + 2

# map applies a function to all the items of a list and returns a modified list
result = list(map(mapper, numbers))

print(result)

# the filter will remove the items that doesn't match with the condition of your function and filter returns a modified list
def bigbro(x):
    if x %2== 0:
        return True
    else:
        return False
result = list(filter(bigbro, numbers))

print(result)

