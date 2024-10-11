import random
x1 = random.randint(1,1000)
x2 = random.randint(1,1000)
x3 = random.randint(1,1000)
print('NUMBERS BEFORE ARRANGEMENT ',x1,x2,x3)
x1,x2,x3=x1,x2,x3
if(x1>x2):
    if(x2>x3):
        x1,x2,x3=x3,x2,x1
    else:
        x1,x2,x3=x2,x3,x1
elif(x2>x3):
    if(x1>x3):
        x1,x2,x3=x3,x1,x2
    else:
        x1,x2,x3=x1,x3,x2
elif(x3>x1):
    if(x2>x1):
        x1,x2,x3=x1,x2,x3
    else:
        x1,x2,x3=x2,x1,x3
print(x1,x2,x3)
    