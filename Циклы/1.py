preferences = input("Введите своё музыкальное предпочтение")
text = "z"
a = 1
while a >= 0:
    text = input("Введите своё музыкальное предпочтение")
    preferences = preferences + ' ' + text
    a -= 1
print(preferences)