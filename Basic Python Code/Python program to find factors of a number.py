---- Using (1,num+1) as Range ----

num=int(input())
factor=[]
for i in range(1,num+1):
    if (num%i==0):
        factor.append(i)
print(factor)

---- Output: -----
15
:=[1, 3, 5, 15]
