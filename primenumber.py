# PRIME NUMBER
n = int(input("Enter a number: "))  # INPUT ELEMENT
if n > 1:
    for i in range(2, n):  # FOR RANGE IN VALUE IN PRIME NOT 2 POWER VAL
        if (n % i) == 0:
            print(n, "is not a prime number")  # PRINT THE N NOT S PRIME VALUE
            print(i, "times", n // i, "is", n)  # PRINT THE RESON OF NOT PRIME
            break  # END THE PROCESS
    else:
        print(n, "is a prime number")  # PRINT THE PRIME VALUE
else:
    print(n, "is not a prime number")  # PRINT THE NOT PRIME VALUE
