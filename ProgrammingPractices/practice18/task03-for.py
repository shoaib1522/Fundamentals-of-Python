n = int(input('N: '))
for i in range(1,n+1):
    for space in range(i-1):
        print(end=' ')
    for plus in range((n+1)-i):
        print('+',end='')
    print()
for k in range(1,n):
    for space2 in range (1,n-k):
        print(end=' ')
    for plus2 in range (k+1):
        print('+',end='')
    print()