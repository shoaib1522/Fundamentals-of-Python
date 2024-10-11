num = int(input('enter the three-digit number'))
a = num // 100
b = num // 10 % 10
c = num % 10
print(f'the reversed number is {c}{b}{a}')