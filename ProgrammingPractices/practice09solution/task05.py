number = int(input('enter the number'))
a = number // 100
print('the first digit is ',a)
b = number // 10 % 10
print('the second digit is ',b)
c = number % 10
print('the third digit is ',c)
print(a+b+c)