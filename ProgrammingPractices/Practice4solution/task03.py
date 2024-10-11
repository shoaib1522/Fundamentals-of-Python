import random
x1=random.randint(1,10)
x2=random.randint(1,10)
x3=random.randint(1,10)
print(x1,x2,x3)
n1=x1-x2
n2=x2-x3
n3=x1-x3
if(n1 >=2 or n1 <= -2) and  (n2 >=2 or n2 <= -2) and  (n3 >=2 or n3 <= -2):
    print('ok')
else:
    print('sorry')