products = input()
listel = products.split()
# a и цифра рядом номер товара по возрастанию
a1, a2, a3 = listel
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
if a1 > a2:
    if a2 > a3:
        print('"Акция!"')
        print((a1 + a2 + a3) / 2)
elif a1 < a2:
    if a2 < a3:
        print('"Акция!"')
        print((a1 + a2 + a3) / 3)
else:
    print('к оплате ', (a1 + a2 + a3))