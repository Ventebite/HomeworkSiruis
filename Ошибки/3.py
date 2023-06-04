try:
    login = input("Введите логин:")
    if not login.islower():
        raise SyntaxError("Все символы должны быть строчными")
    else:
        print("Логин добавлен в базу")
except SyntaxError as e:
    print(e)
finally:
    print("Я выучил исключения")