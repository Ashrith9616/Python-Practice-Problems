---- Using while loop ----

n=int(input())
l=[]
for i in range(2,n):
    while n%i==0:
        l.append(i)
        n=n//i
print(l)

---- Output ----
30
:=[2, 3, 5]
