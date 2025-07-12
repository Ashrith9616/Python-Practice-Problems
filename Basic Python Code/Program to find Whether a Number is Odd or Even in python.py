---- Using Brute Force ----
num = int(input("Enter a Number:")) 
if num % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")

---- Using Ternary Operator ----
num = int(input())
print("Even") if num%2 == 0 else print("Odd")

---- Using Bitwise Operator ----
def isEven(num):
  return num%2==0

if __name__ == "__main__":
  num = int(input())
  if isEven(num):
    print('Even')
  else:
    print('Odd')

---- Output ----
Enter a Number:2
Given number is Even
Enter a Number:3
Given number is Odd
