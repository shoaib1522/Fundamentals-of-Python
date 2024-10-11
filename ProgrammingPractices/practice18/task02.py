rows = int(input('Rows: '))
i=1
while i<=rows:
    j=1
    while j<=i:
        print('+',end='')
        j+=1
    print()
    i+=1
l=1
while l<=(rows-1):
    k=rows-1
    while k>=l:
        print('+',end='')
        k-=1
    print()
    l+=1
    