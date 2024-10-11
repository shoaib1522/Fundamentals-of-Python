rlength1=float(input('enter length of first tri'))
rlength2=float(input('enter length of second tri'))
rwidth2=float(input('enter width of second tri'))
rwidth1=float(input('enter width of first tri'))
area1=rlength1*rwidth1
area2=rlength2*rwidth2
if area1>area2:
    print('second triangle is smaller')
elif area1<area2:
    print('first triangle is smaller')
