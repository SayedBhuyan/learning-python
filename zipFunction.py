rolls = [101,102,103,104,105,106]
names=['sayed','mahmud','hasan','arif','tareq','bhuyan']

students = list(zip(rolls, names, "012012"))
print(students)

r =list(filter((lambda x : int(x[2])==1), students))

l = [each for each in students if int(each[2]) == 0 ]

print(r)
print(l)