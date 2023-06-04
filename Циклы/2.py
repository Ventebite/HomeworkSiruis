start = input()
if start == 'game':
    a = 2
    print('игра Угадай число запушена')
    while a >= 0:
        reple = input()
        if reple == '5':
            print("Вы выиграли билет на концерт!")
            break
        elif reple == 'off':
            print("Вы проиграли")
            break
        a -= 1