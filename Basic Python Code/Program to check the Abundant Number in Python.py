---- Using Range until Number ----

n = int(input("Enter a number: "))
sum = 1 

for i in range(2,n):
  if(n%i==0):  
        sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')
else:
  print(n,'is not Abundant Number')

---- Output -----
Enter a number: 12
:= 12 is Abundant Number

Enter a number: 15
:= 15 is not Abundant Number
