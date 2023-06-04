fulname = input()
fulname = fulname.split()
name = fulname[0]
surname = fulname[1]
patronymic = fulname[2]
print(name, (surname[0]).upper() + '.' + (patronymic[0]).upper() + '.' )