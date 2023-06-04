def negative(colour):
    if colour <= 50:
        print(255, ": Черный становиться белым")
    elif colour == 255:
        print(0, ": Белый становиться черным")
    else:
        print(255 - colour, ": Почти белый становиться очень темным")




colour = int(input())
negative(colour)