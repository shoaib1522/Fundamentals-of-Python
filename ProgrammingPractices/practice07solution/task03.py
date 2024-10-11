import random
x1 = random.randint(1,1000)
x2 = random.randint(1,1000)
x3 = random.randint(1,1000)
print('NUMBERS BEFORE CHECKING ORDER ',x1,x2,x3)
if (x3>x2) and (x2>x1):
    print('Numbers are in order')
else:
    print('Numbers are not in order')