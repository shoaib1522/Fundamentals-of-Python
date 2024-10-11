array_1=[2, 5, 9, 11, 16]
array_2=[3, 10, 18, 19, 20]
sorted_array=[0]*10
for i in range(len(array_2)):
    sorted_array[i]=array_1[i]
for j in range(5,len(array_1)+len(array_2)):
    sorted_array[j]=array_2[j-5]
print('Merged Array: ',sorted_array)
for k in range(len(sorted_array)):
    for l in range(len(sorted_array)-1):
        if sorted_array[l]>sorted_array[l+1]:
            sorted_array[l],sorted_array[l+1]=sorted_array[l+1],sorted_array[l]
print('Sorted Merged Array: ',sorted_array)