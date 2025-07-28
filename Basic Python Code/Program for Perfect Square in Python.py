----- Using Simple iteration ----

import math
num = int(input("Enter a number: "))
x = math.sqrt(num)
y = int(x)
a = y * y

if num == a:
    print("perfect square")
else:
    print("not a perfect square")

---- Output ----

Enter a number: 25
:= perfect square

Enter a number: 10
:= not a perfect square
