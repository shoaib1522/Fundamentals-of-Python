import random
arr = [0] * 20
arr[0] = random.randint(1,10)
for i in range(1, 20):
    arr[i] = arr[i - 1] + random.randint(1,10)
print("Array: ", arr)
miss = []
for i in range(1, 46):
    if i not in arr:
        miss.append(i)
print("Missing values: ", miss)