---- USING BRUTE FORCE ----
num = int(input())
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print('Zero')

---- USING Nested if-else Statements -----
num = int(input())
if num>=0:
    if num==0:
        print('Zero')
    else:
        print("Positive")
else:
    print("Negative")

---- USING TERNARY OPERATORS ----
num = int(input())
print("Positive" if num>=0 else "Negative")

---- Output: ----
8 
positive
-9
negative
