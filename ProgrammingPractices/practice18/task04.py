n = int(input('N: '))
i=1 
while i<=n:
    plus_1=1
    while plus_1<=(n+1)-i:
        print('+',end='')
        plus_1+=1
    space=1
    while space<=(i-1)*2:
        print(end=' ')
        space+=1
    plus_2=(n+1)-i
    while plus_2>=1:
        print('+',end='')
        plus_2-=1
    print()
    i+=1
j=1
while j<=(n-1):
    plus_3=1
    while plus_3<=(j+1):
        print('+',end='')
        plus_3+=1
    space_2=1
    while space_2<=((n+3)-(j*2)):
        print(end=' ')
        space_2+=1
    plus_4=1
    while plus_4<=(j+1):
        print('+',end='')
        plus_4+=1        
    print()
    j+=1
    