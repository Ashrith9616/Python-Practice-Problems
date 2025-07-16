---- Using For Loop Iteration between [1, num] -----

n = int(input())
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

---- Output ----
28
:= The number is a Perfect number
10
:= The number is not a Perfect number
