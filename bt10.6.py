import math
x = int ( input (' nhập số x: '))
y = int ( input (' nhập số y: '))
z = int ( input (' nhập số z: '))
if x == 0:
    print (' phương trình sai rồi nha ')
else:
    delta = pow (y, 2) - 4*x*z
    if delta < 0:
        print (' phương trình vô nghiệm ')
    elif delta == 0:
        print (' phương trình có nghiệm kép a1 = a2 = ', -y/2*x)
    else:
        print (' phương trình có hai nghiệm a1 = ', (-y-math.sqrt(delta))/2*x,
         'và a2 =', (-y+math.sqrt(delta))/2*x)