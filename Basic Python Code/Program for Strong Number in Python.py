----- Using Loop ----

import math
num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += math.factorial(digit)
    temp = temp // 10

if sum == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")

---- Output ----
Enter a number: 15
:= 15 is not a strong number
Enter a number: 145
:= 145 is a strong number
