num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqNum = list(map((lambda x : x * x), num))
print((sqNum))

sqNum2 = [val * val for val in num]
print(sqNum2)


evenNum = list(filter((lambda x : x % 2 == 0), num))
print(evenNum)



evenNum2 = [each for each in num if each % 2 == 0]
print(evenNum2)

