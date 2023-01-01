# Tính tổng số nguyên N nhập vào, chấm dứt khi kết thúc là số 0
def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + (12%10) + (34%10) + (25%10) +  (0%10) 
        n = int(n / 10)
    return total
n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n))
