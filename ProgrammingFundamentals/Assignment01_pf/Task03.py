import random
original_array = [random.randint(0,10) for i in range(10)]
new_array = [0] * len(original_array)
for i in range(len(original_array)):
    new_array[i] = original_array[i]
print("Original array:", original_array)
print("New array:", new_array)
