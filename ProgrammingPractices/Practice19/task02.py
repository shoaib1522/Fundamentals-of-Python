def print_char(c,n):
    for i in range(n):
        print(c , end=' ')

def main():
    c=input('Enter the character you want to print: ')
    n=int(input('Tell hoe many times you want ot print it: '))
    print_char(c,n)
main()