---- Using if-else Statements ----
num1 = int(input())
num2 = int(input())
num3 = int(input())
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

---- Using Nested if-else Statements ----
num1 = int(input())
num2 = int(input())
num3 = int(input())
max = 0
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)

---- Output ----
34
45
12
:= 45
