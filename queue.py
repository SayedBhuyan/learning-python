from collections import deque

bankLine = deque(["Sayed", "Karim", "Rahim", "Rafi"])

print(bankLine)

bankLine.popleft()
print(bankLine)

bankLine.popleft()
print(bankLine)

bankLine.popleft()
print(bankLine)

bankLine.popleft()
print(bankLine)

if not bankLine:
    print("No person left")