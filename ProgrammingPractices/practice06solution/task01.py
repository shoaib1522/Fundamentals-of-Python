import random
x=random.randint(1,5)
y=random.randint(1,5)
print('first number',x)
print('second number',y)
subtract=abs(x-y)
if subtract<=1:
    print('equal almost')
else:
    print('Not equal')
