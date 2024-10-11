a = float(input('enter value of a'))
b = float(input('enter value of b'))
c = float(input('enter value of c'))
disc = (b*b-4*a*c)
if (a==0):
    print('Equation you entered is linear')
elif (disc<0):
    print('Roots are imaginary')
else:
    print ('x1',(-b+disc**0.5)/(2*a))
    print ('x2',(-b-disc**0.5)/(2*a))
