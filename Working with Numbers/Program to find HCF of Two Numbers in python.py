---- Linear Quest to find HCF ----

num1 = int(input("Enter the Number: "))
num2 = int(input("Enter the Number: "))
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)

---- Output -----
Enter the Number: 4
Enter the Number: 4
:= Hcf of 4 and 4 is 2
