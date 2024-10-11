import random
i=1
rows=int(input('Rows: '))
colums=int(input('Columns: '))
while i<rows:
    j=1
    while j<colums:
        x=random.randint(10,90)
        print(x,end=' ')
        j+=1
    print()
    i+=1