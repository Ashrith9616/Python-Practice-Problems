---- Using inner loop Range as [2, number-1] ----
low = int(input())
high = int(input())
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)

---- Output ----

2
10
:=[2, 3, 5, 7]
