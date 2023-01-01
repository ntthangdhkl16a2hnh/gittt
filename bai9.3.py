# Tính chỉ số BMI
import math
a=float(input("Nhập cân nặng(kg):" ))
b=float(input("Nhập chiều cao(m):"))
c=a/(b*b)
print("chỉ số BMI của bạn là:",BMI)
if c<18.5:
    print("Bạn gầy quá")
elif c<=24.99:
    print("Cơ thể của bạn bình thường")
elif c>=25:
    print("Bạn bị thừa cân")