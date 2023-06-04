"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
vocabl = {"1":1, "2":2, "3":3, "4":4, "5":5}
first_key, last_key = list(vocabl)[0], list(vocabl)[-1]
vocabl[first_key], vocabl[last_key] = vocabl[last_key], vocabl[first_key]
del vocabl[list(vocabl)[1]]
vocabl["new_key"] = 'new_value'
print(vocabl)