def thesaurus(*args):
    new_list = {}
    for i in sorted(args):
        new_list.setdefault(i[0], [])
        new_list[i[0]].append(i)
    return new_list


#Для проверки
print(thesaurus("Иван", "Мария", "Петр", "Илья"))
