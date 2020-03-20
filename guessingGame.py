from random import randint

won = 0
lost = 0

for x in range(1, 6) :
    guessingNumber = int(input("Enter a number between 1 - 5: "))
    randomNumber = randint(1,5)

    if guessingNumber == randomNumber:
        won = won + 1
        print("You have won with ",guessingNumber,", random rumber was ",randomNumber)
    else:
        lost = lost + 1
        print("You have lost with ",guessingNumber,", random rumber was ",randomNumber)


print("\n\n")
print("You won ", won , " times, and you lost ", lost, " times. ")