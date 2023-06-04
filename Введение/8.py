number = int((input("Введите число:")))
one = number // 100 % 10
two = number // 10 % 10
three = number % 100 % 10
print (one + two + three)