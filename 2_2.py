info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
correct_info = []
for i in info:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            correct_info.append(f"'{int(i):02}'")
        else:
            correct_info.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        correct_info.append(i)

print(correct_info)
print(" ".join(correct_info))
