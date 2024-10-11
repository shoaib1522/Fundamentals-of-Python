n=int(input('N: '))
k=int(input('K: '))
i=1
print('{',end='')
while i<=n:
    j=1
    while j<=k:
        print(f'({i},{j})',end='')
        j+=1
        print(',',end='')
    i+=1
print('}')