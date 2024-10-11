n = int(input('N: '))
i=1
while i<=n:
    k=1
    while k<=(i-1):
        print(end=' ')
        k+=1
    j=(n+1)-i
    while j>=1:
        print('+',end='')
        j-=1
    print()
    i+=1
lun =1
while lun<=(n-1):
    h=n-lun
    while h>=2:
        print(end=" ")
        h-=1
    b=1
    while b<=(lun+1):
        print('+',end='')
        b+=1
    print()
    lun+=1