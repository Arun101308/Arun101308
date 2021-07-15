arr = (input("elements").split())  # INPUT ELEMENTS
temp = 0;  # TEMP VEL 0
i, j = input(), input()  # INPUT OF ELEMENT VALUE
print("Elements of original array: ");
for i in range(0, len(arr)):  # RANGE VALUE TOTAL ELEMENTS
    print(arr[i]),
for i in range(0, len(arr)):  # DESCENDING ORDER RANGE I VALUE
    for j in range(i + 1, len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Elements of array sorted in descending order: ");
for i in range(0, len(arr)):
    print(arr[i])  # PRINT OUTPUT
    for i in range(0, len(arr)):  # ASCENDING ORDER RANGE IN I VALUE
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
print("Elements of array sorted in ascending order: ");
for i in range(0, len(arr)):
    print(arr[i]);  # PRINT OUTPUT
