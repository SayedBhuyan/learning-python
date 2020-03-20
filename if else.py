#mark = int(input("Enter Mark: "))

# if else
mark = 85

if mark >= 80:
    print("A+")
elif mark >= 70:
    print("A")
elif mark >= 60:
    print("A-")
elif mark >= 50:
    print("B+")
elif mark >= 40:
    print("B")
elif mark >= 33:
    print("B-")
else:
    print("Fail")

'''
if (mark % 2) == 0:
    print("Even")
else :
    print("Odd")
    
    '''


# nested if statement

if 5 > 2:
    if 7 > 2:
        print("good")
    else:
        print("Not matched")
else :
    print("Not a even")

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else :
        print(num3)