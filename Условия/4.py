category = input("Введите категорию товара").lower()
if category == "продукты":
    playment = float(input('Введите цену'))
    if playment < 100:
        print('"Попробуй нашу выпечку"')
    elif playment < 500:
        print('"Как насчёт орехов в шоколаде?"')
    elif playment >= 500:
        print('"Попробуйте экзотические фрукты!"')
else:
    print('"Загляните в товары для дома!"')