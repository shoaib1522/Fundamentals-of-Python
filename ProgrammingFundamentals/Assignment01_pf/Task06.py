import random
arr = []
while len(arr) < 10:
    num = random.randint(1, 15)
    if num not in arr:
        arr.append(num)
print(arr)
