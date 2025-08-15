---- Using Simple Iteration ----
num = int(input())
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

---- Output ----
10  
Fibonacci Series: 0 1 1 2 3 5 8 13 21 34 
