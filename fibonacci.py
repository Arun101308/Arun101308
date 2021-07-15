n = int(input("ENTER NUMBER")) # INPUT VALUE
def fibonacci(n):  # FIBONACCI IN VAL N
    a = 0
    b = 1
    if n < 0: # IF VAL N GRATERTHEN 0
        print("Incorrect input")
    elif n == 0: # ELSE IF N INEQUALEN 0
        return 0
    elif n == 1: # ELIF N INEQUALEN 1
        return b
    else:
        for i in range(1, n): # FOR I IN RANGE VALUE IS 1,N
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(n)) #PRINT OUTPUT
