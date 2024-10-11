n = int(input('N: '))
for i in range(1,n+1):
    for plus1 in range((n+1)-i):
        print(end='+')
    for space1 in range((i-1)*2):
        print(end=' ')
    for plus2 in range((n+1)-i):
        print(end='+')
    print()
for j in range(1,n):
    for plus3 in range(j+1):
        print(end='+')
    for space2 in range((n+3)-(j*2)):
        print(end=' ')
    for plus4 in range(j+1):
        print(end='+')
    print() 