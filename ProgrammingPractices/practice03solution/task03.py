x = int(input('Input the value of x'))
y = int(input('Input the value of y'))
cub_x = x*x*x
cub_y = -y*y*y
dub_x = -3*x*x*y
dub_y = 3*x*y*y
x_y = cub_x+dub_x+dub_y+cub_y
print('hence the calue of (x-y)^3 is: ',x_y)
