import math
A= lambda x,n: math.pow((x*x+x+1),n) + math.pow((x*x-x+1),n)
print("A=" ,A(3,6))