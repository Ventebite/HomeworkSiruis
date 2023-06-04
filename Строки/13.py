text = input()
act1 = text.split("@")
act2 = act1[0]
act3 = act2.split(" ")
act4 = act3[-1]
act5 = act1[1]
act6 = act4.split(' ')
act7 = act6[0]
print(act4 + '@' + act7)