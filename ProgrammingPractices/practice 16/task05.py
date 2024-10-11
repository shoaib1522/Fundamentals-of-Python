rows=int(input('Rows: '))
x=1
i=1
while i<=rows:
    j=1
    while j<=5:
        print(x,end=' ')
        x+=1
        j+=1
    x=0
    print()
    i+=1
    x+=i