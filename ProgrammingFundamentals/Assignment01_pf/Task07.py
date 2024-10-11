import random

arr = [random.randint(1, 5) for i in range(10)]
print("Initial array:", arr)

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            print("Element", arr[i], "exists at indices", i, "and", j)
