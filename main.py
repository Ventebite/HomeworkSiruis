'''#Задание 1 06.03.23
games = []
game = input()
while game != '0':
    games.append(game)
    game = input()
    if game in games:
        print('Эта игра уже записана')
    games.sort()
print(*games)
'''
'''#Задание 2
estimated = input()
estimated = estimated.split(',')
estimated = list(map(int, estimated))

print((estimated.count(5) + estimated.count(4) + estimated.count(3))/ len(estimated) * 100)'''
'''#Задание 3
estimated = input()
estimated = estimated.split(',')
estimated = list(map(int, estimated))
reqor = input()
if reqor == ' ':
    print("Чило пятёрок ", estimated.count(5), ". ", "Процент полученых пятёрок ", estimated.count(5)/
          len(estimated) * 100)
'''
'''#Задание 4
liste = []
ltlastname = input("Введите Фамилию преподавателя")
lastname = []
lastname.append(ltlastname)
ltpost = input("Введите должность")
post = []
post.append(ltpost)
ltnamber_group = input("Введите кол-во студентов всех групп")
namber_group = []
namber_group.append(ltnamber_group)
liste.append(lastname)
liste.append(post)
liste.append(namber_group)
print(liste)
'''
#Задание 5
nambers = input()
nambers = nambers.split(',')
nambers = list(map(int, nambers))


'''#Задание 1 21.02.23
preferences = input("Введите своё музыкальное предпочтение")
text = "z"
a = 1
while a >= 0:
    text = input("Введите своё музыкальное предпочтение")
    preferences = preferences + ' ' + text
    a -= 1
print(preferences)
'''
''' #Задание 2
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
'''
'''#Задание 3
log = list(input('Нельзя использоват символы', '=?*^$№@_'))
for i in log:
    if i in '=?*^$№@_':
        print('Запрещённые символ(-ы):', i)
        break
'''
'''#Задание 4
feedback = input("Оставте свой отзыв")
a = 2
while a >= 0:
    print('Спасибо, ваш отзыв принят!')
    feedback = input("Оставте свой отзыв")
    if feedback == 'off':
        break
'''



'''#Задание 1 18.02.23
eat = input()
if eat == 'Завтрак':
    print('каша')
elif eat == "Обед":
    print("плов")
else:
    print("котлета с пюре")'''
'''#Задание 2
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
print('Мы закрыты')'''
'''#Задание 3
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
    print('к оплате ', (a1 + a2 + a3))'''
'''
#Задание 4
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
'''
'''
#Задание 5
namber = input()
intnamber = int(namber)
nam = namber[1:]
if int(nam) / 2 >= 0:
    print("Число четное")
    if sum(map(int, namber)) / 6:
        print("Число делится на 6")
    else:
        print("ERROR")
else:
     print("Число не делится на 6")
     '''

''' Задание 1 04.02.23
stringa = input()
stringb = input()
print(stringa + stringb)'''
''' Задание 2
nam = int(input())
print('r' * nam)'''
''' Задание 3
stringa = input()
print(stringa[::-1])'''
''' Задание 4
stringa = input()
stringa = stringa.split()
print(stringa[1], stringa[0])'''
''' Задание 5
stringa = input()
stringa = stringa.split('@')
print(stringa[0])'''
''' Задание 6
stringa = input()
print(stringa[2] + stringa[3] + stringa[4])'''
''' Задание 7
fulname = input()
fulname = fulname.split()
name = fulname[0]
surname = fulname[1]
patronymic = fulname[2]
print(name, (surname[0]).upper() + '.' + (patronymic[0]).upper() + '.' )'''
'''Задание 8
stringa = input()
redact = stringa.replace('ический', '.')
end = redact.replace('ическая', '.')
print(end)'''
''' Задание 9
stringa = input()
dash = stringa.replace('--', '— ')
print(dash)'''
''' Задание 10
stringa = input()
scraping = stringa.replace('(', '').replace(')', '').replace('-', '')
#end = scraping.join('.')
print(scraping.replace(' ', ''))'''
''' Задание 11
namber = input()
print('<a href="tel:' + namber + ' "> ' + namber + ' </a>')'''
'''#Задание 12
stringa = input()
scraping = int(stringa.replace('<span>', '').replace('&nbsp', '').replace(';', '').replace('P</span>', ''))
print(scraping + 1)'''
'''#Задание 13
text = input()
act1 = text.split("@")
act2 = act1[0]
act3 = act2.split(" ")
act4 = act3[-1]
act5 = act1[1]
act6 = act4.split(' ')
act7 = act6[0]
print(act4 + '@' + act7)'''

''' Задача 1 23 Января
print(16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24)'''
''' Задача 2
a = int(input())
b = int(input())
print(a + b)
'''
''' Задача 3
def negative(colour):
    if colour <= 50:
        print(255, ": Черный становиться белым")
    elif colour == 255:
        print(0, ": Белый становиться черным")
    else:
        print(255 - colour, ": Почти белый становиться очень темным")




colour = int(input())
negative(colour)
'''
''' Задача 4
liste = []
a = int(input())
b = int(input())
c = int(input())
liste.append(a)
liste.append(b)
liste.append(c)
print(sum(liste))
print(max(liste))
print(min(liste))
'''
''' Задача 5
liste = []
a = int(input())
b = int(input())
liste.append(a)
liste.append(b)
print(max(liste) - min(liste))
'''
''' Задача 6 не знаю, как решить
rubdol = float(input())
dolev = float(input())
evrub = 
print(round(evrub, 2))'''
''' Задача 7
items = int(input())
if items == 0:
    print(0)
else:
    print(int(1572 / items))'''
'''#Задача 8 не понимаю, как сделать без циклов
namber = int(input())
liste = []
factor = []
liste.append(namber)
print(count(liste))
'''
''' Задание 9 не понимаю, как решить только с операциями на числа
nam1 = input()
liste = list(nam1)
print(nam1, liste)
liste.reverse()
print(*liste)
'''
'''Задание 10 не понимаю'''
''' Задача 11
m = int(input())
h = int(input()) / 100
namber = m / h ** 2
print(round(namber, 2)) '''
'''Задание 12 не знаю, как выполнить
widtw = float(input())
height = float(input())
expend = int(input())
volume = int(input())
reserve = int(input())'''