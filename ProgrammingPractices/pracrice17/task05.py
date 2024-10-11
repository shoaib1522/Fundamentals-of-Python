rows=int(input('Rows: '))
col=int(input('Columns: '))
i=1
while i<=rows:
    j=1
    while j<=col-1:
        print(' ',end=' ')
        j+=1
    print(i)
    i+=1 