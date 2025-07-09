---- Using Repeated Subtraction ----

num1 = int(input())
num2 = int(input())
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("GCD of", a, "and", b, "is", num1)

---- Output ----
12
24
GCD of 12 and 24 is 12
