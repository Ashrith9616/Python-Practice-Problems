----- Using Simple Iteration ----
num = int(input())
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

---- Output ----
12345
:= 54321
