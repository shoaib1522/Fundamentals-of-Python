import random
l = [random.randint(1,10) for i in range(10)]
i=9
while i>=0:
    print(l[i],end=' ')
    i-=1