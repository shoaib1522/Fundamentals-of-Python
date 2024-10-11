import random
array=[random.randint(0,9) for i in range(20)]
array_2=[array[k] for k in range(len(array))]
for i in range(len(array)):
    print(array[i],end=' ')
print()
for averaging in range(2,18):
    avg=(array[averaging-2]+array[averaging-1]+array[averaging+1]+array[averaging+2])//4
    array_2[averaging]=avg
for i in range(len(array)):
    print(array_2[i],end=' ')