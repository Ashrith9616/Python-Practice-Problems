---- Method 1 -----
low = int(input())
high = int(input())

for n in range(low, high + 1):

    # order of number
    order = len(str(n))

    # initialize sum
    sum = 0

    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if n == sum:
        print(n, end=", ")

---- Output ----
0
10000
:= 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474,
