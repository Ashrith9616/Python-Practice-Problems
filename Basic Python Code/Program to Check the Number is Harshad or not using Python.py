---- Using simple Iteration ----

N=input(“Enter a number:”)
sum=0
for i in N:
    sum+=int(i)
if int(N)%sum==0:
    print("Harshad number")
else:
    print("Not a Harshad Number")

---- Output ----
Enter a number:18
:= Harshad number

Enter a number:25
:= Not a Harshad Number
