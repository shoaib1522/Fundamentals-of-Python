n=int(input('N: '))
i=1
while i <= n:
    character = 97
    while character<=122:
        print(chr(character),end=' ')
        character+=i
    print()
    i+=1
