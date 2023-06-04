a = []
while True:
    price = int(input())
    if price == 0:
        break
    a.append(price)


print(sum(a))
print(sum(a) - ((sum(a) / 100) * 20))