char_1= input('input your character 1 ')
char_2=input('input your character 2  ')
char1 = (ord(char_1))
char2 = (ord(char_2))
count=0
if char1 & 1==char2 & 1: 
    count=count+1
if char1 & 2== char2 & 2:
    count=count+1
if char1 & 4==char2 & 4:
    count=count+1
if char1 & 8==char2 & 8:
    count=count+1
if char1 & 16== char2 & 16:
    count=count+1
if char1 & 32== char2 & 32:
    count=count+1
if char1 & 64==char2 & 64:
    count=count+1
print('the number of bits which are same are',count)