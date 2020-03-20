# Factorial n!



n = int(input("Enter factorial number: "))
sum = 1

for x in range(1, n + 1, 1) :
    sum = sum * x
print(sum)

