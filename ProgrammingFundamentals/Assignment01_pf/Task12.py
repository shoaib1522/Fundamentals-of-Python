import random
array=[random.randint(3,7) for i in range(10)]
print(array)
for i in range(len(array)):
    sum=0
    for j in range(i+1):
        print(array[j],end=' ')
        sum+=array[j]
    print('=',sum)