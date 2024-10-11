rows = int(input('Rows: '))
for i in range(1,rows+1):
    for space in range(i-1):
        print(end=' ')
    print(i)