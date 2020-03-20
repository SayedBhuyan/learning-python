import re

pattern = r"color"

str = "I love green color, My garden is green color."

is_matched = re.match(pattern, str)
if is_matched:
    print("Matched")
else:
    print("Not matched")


is_matched = re.search(pattern, str)
if is_matched:
    print("Matched: ", is_matched.start())
    print("Matched: ", is_matched.end())
    print("Matched: ", is_matched.span())
else:
    print("Not matched")

finds = re.findall(pattern, str)
print(finds)


str2 = re.sub(pattern, "colour", str, count=1)
print(str2)
