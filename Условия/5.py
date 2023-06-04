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