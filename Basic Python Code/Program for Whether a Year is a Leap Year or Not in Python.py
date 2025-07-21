---- Using if-else statements (1) ----
year = int(input())
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

----  Using if-else statements (2) ----
year = int(input())
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not a leap Year")

---- Output ----
2024
:= Leap Year
2018
:= Not a Leap Year
