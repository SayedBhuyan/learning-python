# try :
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     res = num1 / num2
#
#     print(res)
#
# except (ValueError,ZeroDivisionError):
#     print("There was a problem. Please try again with different input")


age = int(input("Enter your age: "))

def voterCheck(a):
    if a < 18:
        raise ValueError("You're not allowed to vote.")
    return "You can vote"


try:
    print(voterCheck(age))
except ValueError as e:
    print(e)
