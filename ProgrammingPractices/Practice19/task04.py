def print_sum_and_return(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def main():
    n=int(input('How much first n integers sum you want to print: '))
    print('The sum of first',n,'integers',print_sum_and_return(n))
main()