import random
i=1
while i<=10:
    x=random.randint(1,20)
    y=random.randint(1,20)
    if x>y:
        print('first number is maximum')
    else:
        print('second number is maximum')
    i+=1