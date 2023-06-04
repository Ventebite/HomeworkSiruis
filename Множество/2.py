"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
my_set = set(testList)
types = [list, set, dict]
for element in my_set:
    if type(element) in types:
        print(False, element)
        break
else:
    print(True)