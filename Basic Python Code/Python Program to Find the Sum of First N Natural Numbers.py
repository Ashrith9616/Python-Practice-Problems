 ---- Using for Loop ----
num = int(input())
sum = 0
for i in range(num+1):
  sum+=i
print(sum)

-----Using Formula for the Sum of Nth Term----
num = int(input())
print(int(num*(num+1)/2))

---- Using Recursion ----
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = int(input())
print(getSum(num))


---- OUTPUT: ----
8
36
