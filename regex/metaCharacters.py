import re

# pattern = r"^col..ur$"

# pattern = r"ice(-)?cream"

# str = "ice-cream"

# pattern = r"a{1,3}$"
# str = "aaaa"


# pattern = r"[A-Z][a-z][0-9]"
# str = "Aa0 quick brown fox"

pattern = r"\+*1*[0-9]{3}-*\s*[0-9]{3}-*\s*[0-9]{4}"
str = "+1954 934 6984"
is_matched = re.match(pattern, str)
if is_matched:
    print("Matched")
else :
    print("Not matched")



str2 = re.sub(pattern, "9549345584", str)
print(str2)