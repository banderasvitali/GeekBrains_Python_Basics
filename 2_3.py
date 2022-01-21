info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
for element in info:
    if len(element) > 1:
        for letters in element:
            if letters == "-" or letters == "+":
                info[i] = '"' + element.zfill(3) + '"'
                break
            elif 47 < ord(letters) < 58:
                info[i] = '"' + element.zfill(2) + '"'
                break
    elif len(element) <= 1 and 47 < ord(element) < 58:
        info[i] = '"' + element.zfill(2) + '"'
    i += 1
print(" ".join(info))
