----- Using Simple iterative solution ----

num = int(input())
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")

---- Output ----
13
:= Prime
15
:= Not Prime
