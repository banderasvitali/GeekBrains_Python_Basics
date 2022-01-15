for i in range(100):
    i = i + 1
    if 11 <= i < 15:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif 5 > i % 10 > 1:
        print(i, "процента")
    else:
        print(i, "процентов")
