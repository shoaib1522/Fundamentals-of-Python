rows = int(input('Rows: '))
for i in range(rows):
    for j in range(i+1):
        print('+',end='')
    print()
for k in range(1,rows):
    for l in range(rows,k,-1):
        print('+',end='')
    print()
        