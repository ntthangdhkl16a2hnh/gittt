so_kw=int(input("Số KW điện tiêu thụ:"))
if so_kw>0:
    if 0<= so_kw <= 50:
        tongsotien=so_kw*1678
    if 51<= so_kw <=100:
        tongsotien=1678*50 + 1734*(so_kw-50)
    if 101<= so_kw <=200:
        tongsotien=1678*50 + 1734*50 + 2014*(so_kw-100)
    if 201<= so_kw <=300:
        tongsotien=1678*50 + 1734*50 + 2014*100 + 2536*(so_kw-200)
    if 301<= so_kw <=400:
       tongsotien=1678*50 + 1734*50 + 2014*100 + 2536*100 + 2384*(so_kw-300)
    if 401 <= so_kw:
        y=1678*50 + 1734*50 + 2014*100 + 2536*100 + 2384*100 + 2972*(so_kw-400)
    print('Tiền điện là',tongsotien,'đồng.')
        
        
        