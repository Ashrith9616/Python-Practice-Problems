---- Using the Range until Number ---- 

def printDivisors(n, factors) :
    i = 1
    while i <= n :
        if (n % i==0) :
            factors.append(i)
        i = i + 1
    return sum(factors) - n

if __name__ == "__main__": 
  number1 = int(input("Enter a number1: "))
  number2 = int(input("Enter a number2: "))
  if int(printDivisors(number1, [])/number1) == int(printDivisors(number2, [])/number2):
    print("Friendly pair")
  else:
    print("Not a Friendly Pair")

----- Output ----
Enter a number1: 224
Enter a number2: 280
Friendly pair

Enter a number1: 225
Enter a number2: 260
Not a Friendly Pair
