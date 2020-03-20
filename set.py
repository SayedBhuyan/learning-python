numbers = {1, 2, 3, 4, 5}

numbers2 = set([1, 2, 3, 4, 5, 6, 7])
numbers2.add(8)
numbers2.remove(8)

union = numbers | numbers2
intersection = numbers & numbers2
difference = numbers2 - numbers
print(union)
print(intersection)
print(difference)