# Tính diện tích tam giác
import math
a = int(input("nhập độ dài cạnh a :"))
b = int(input("nhập độ dài cạnh b :"))
c = int(input("nhập độ dài cạnh c :"))
cv = a + b + c
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p -c))
print("chu vi hình tam giác :", cv)
print("diện tích hình tam giác :", s)