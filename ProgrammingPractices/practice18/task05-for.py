
def main():
    n=int(input('N: '))
    for i in range(1, n+1):
        for j in range(ord('a'), ord('z')+1, i):
            print (chr(j), end= ' ')
        print()
main()