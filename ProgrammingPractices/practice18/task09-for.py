rows = int (input('Row: '))
for i in range(1,rows+1):
    for space in range(rows-i):
        print(end=' ')
    print(i)