def print_name(name_1, name_2, name_3):
    while name_1 or name_2 or name_3 != "None":
        name_1 = input("name1:")
        name_2 = input("name2:")
        name_3 = input("name3:")
        print(name_1, name_2, name_3)
        if name_1 or name_2 or name_3 == "None":
            break
print_name("a", "b", "c")