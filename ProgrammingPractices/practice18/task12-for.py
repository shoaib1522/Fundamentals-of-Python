rows=int(input('Rows: '))
cols = int(input('Columns: '))
for i in range(1,rows+1):
    n=i
    for number in range(cols):
        print(n,end=' ')
        n+=1
    print()
    character=96+i
    for char in range(1,cols+1):
        print(chr(character),end=' ')
        character+=1
    print()