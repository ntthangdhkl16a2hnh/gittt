 # Tìm ước chung lớn nhất
a = int(input(" Nhap vao so nguyen duong a = "))
b = int(input(" nhap vao so nguyen duong b = "))
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print('Uoc so chung lon nhat cua a va b la: ', uscln(a, b))

 