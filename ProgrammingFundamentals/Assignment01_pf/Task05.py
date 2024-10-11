import random
array=[random.randint(4,87) for i in range(10)]
print('Generated array: ',array)
odd_array=[]
even_array=[]
for i in range(len(array)):
    if (array[i])//2==0:
        even_array.append(array[i])
    if (array[i])//2!=0:
        odd_array.append(array[i])
if len(odd_array)>len(even_array):
    for j in range(len(array)):
        array[j]=array[j]-1
elif len(odd_array)<len(even_array):
    for k in range(len(array)):
        array[k]=array[k]+1
print('Elemented array: ',array)