import random
i=1
while i<=10:
    x=random.randint(1,15)
    y=random.randint(1,15)
    z=random.randint(1,15)
    print('Before arrangement:')
    print(f'x is {x} , y is {y} ,z is {z}')
    if x>y:
        x,y=y,x
    if y>z:
        y,z=z,y
    if x>y:
        x,y=y,x
    print('after arrangement:')
    print(f'x is {x} , y is {y} ,z is {z}')
    i+=1