import random
n1=random.randint(1,1000)
n2=random.randint(1,1000)
n3=random.randint(1,1000)
n4=random.randint(1,1000)
print('numbers before ordering are',n1,n2,n3,n4)
if n1 > n2:
    n1,n2=n2,n1
if n2 > n3:
    n2,n3=n3,n2
if n3 > n4:
    n3, n4 = n4, n3
if n1 > n2:
    n2, n1 = n1, n2
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1,n2=n2,n1
print ('Numbers after ordering')
print (f'N1: {n1}\t\tN2: {n2}\t\tN3: {n3}\t\tN4: {n4}')