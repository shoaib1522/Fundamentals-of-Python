rows=int(input('Rows: '))
cols = int(input('Columns: '))
for i in range(1,rows+1):
    for number in range(1,cols+1):
        print(i,end='')
    print()
    for character in range(1,cols+1):
        print(f'{chr(96+i)}',end='')
    print()