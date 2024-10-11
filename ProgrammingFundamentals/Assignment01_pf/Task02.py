import random
l = [random.randint(1,10) for i in range(10)]
sum=0
i=9
while i>=0:
    sum+=l[i]
    i-=1
print('Sum is ',sum)