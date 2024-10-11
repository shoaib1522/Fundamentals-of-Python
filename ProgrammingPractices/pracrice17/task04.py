rows=int(input('Rows: '))
col=int(input('Columns: '))
i=1
x=1
while i<=rows:
    j=1
    while j<=col:
        print(x,end=' ')
        j+=1
        x+=1
    x=0
    print()
    i+=1
    x+=i