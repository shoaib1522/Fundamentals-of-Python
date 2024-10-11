rows = int(input('Rows: '))
cols = int(input('Columns: '))
for i in range(1,rows+1):
    num = i
    for j in range(1,cols+1):
        print(num,end=' ')
        num+=1
    print()