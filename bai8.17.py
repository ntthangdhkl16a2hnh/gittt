# Tìm bội số chung nhỏ nhất
a = int(input(" Nhap vao so nguyen duong a = "))
b = int(input(" nhap vao so nguyen duong b = "))
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
def bscnn(a, b):
    return int((a * b) / uscln(a, b))  
print('Uoc so chung lon nhat cua a va b la: ', uscln(a, b))
print('Boi so chung nho nhat cua a va b la: ', bscnn(a, b))

 