"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк.
В остальных случаях введенные числа суммируются.
"""
a = input()
b = input()
try:
    print(int(a) + int(b))
except:
    print(a + b)
