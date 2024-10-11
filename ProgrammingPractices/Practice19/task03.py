def print_n_integers_with_d(n,d):
    number = 1
    for i in range(n):
        print(number,end=' ')
        number+=d

def main():
    n=int(input('Enter number of integers you want to print: '))
    d=int(input('Enter the distance between them: '))
    print_n_integers_with_d(n,d)
main()