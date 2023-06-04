log = list(input('Нельзя использоват символы', '=?*^$№@_'))
for i in log:
    if i in '=?*^$№@_':
        print('Запрещённые символ(-ы):', i)
        break