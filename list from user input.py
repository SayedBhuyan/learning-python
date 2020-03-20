# numbers = input("Enter numbers with space to sum: ")
# list = numbers.split()
# sum = 0;
#
# for val in list :
#     sum = sum + int(val);
#
# print(sum)


numberOfLetters = 0
numberOfDigits = 0
numberOfWords = 0

text = input("Enter your text: ") # My name is 123

for val in text :
    val = val.lower()
    if val >= 'a' and val <= 'z' :
        numberOfLetters = numberOfLetters + 1
    elif val >= '0' and val <= '9' :
        numberOfDigits = numberOfDigits + 1
    elif val == ' ' :
        numberOfWords = numberOfWords + 1
print("Letters: ", numberOfLetters)
print("Digits: ", numberOfDigits)
print("Words: ", numberOfWords + 1)