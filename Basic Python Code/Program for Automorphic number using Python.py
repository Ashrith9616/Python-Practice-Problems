----  Using endswith() method ----

num = int(input())
a = str(num)

num1 = num ** 2
b = str(num1)

if b.endswith(a):
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")

---- Output ----
76
:= It's an Automorphic Number
50
:= It's not an Automorphic Number
