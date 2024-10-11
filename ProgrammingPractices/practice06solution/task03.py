import random
marks=random.randint(0,100)
print('Marks:',marks)
if marks>=85:
    print(' the grade is A')
elif marks>=80:
    print('the grade is A-')
elif marks>=75:
    print('the grade is  B+')
elif marks>=70:
    print('the grade is B')
elif marks>=65:
    print('the grade is B-')
elif marks>=61:
    print('the grade is C+')
elif marks>=58:
    print('the grade is C')
elif marks>=55:
    print('the grade is C-')
elif marks>=50:
    print('the grade is D')
elif marks<50:
    print('the grade is F')
