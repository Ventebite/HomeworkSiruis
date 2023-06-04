payment = float(input())
time = float(input())
if time >= 8 and time <= 22:
    if time >= 10:
        if time <= 12:
            print(payment / 2)
    if time >= 20:
        if time <= 22:
            print(payment / 4)
    else:
        print(payment)
print('Мы закрыты')