import random
marks1=random.randint(0,100)
marks2=random.randint(0,100)
print('Marks-1:',marks1,end='')
print(' Marks-2:',marks2)
if (marks1==marks2):
    print('same')
elif(abs(marks1-marks2)<=1):
    print('almost same')
else:
    print('Totally different')
