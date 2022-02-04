from sys import argv

with open("bakery.csv", encoding="utf-8") as b:
    if 1 < len(argv) < 4:
        if len(argv) == 3:
            start, stop = map(int, argv[1:])
            print(*(v for i, v in enumerate(b) if start -1 <= i < stop), end="")
        else:
            print(*(v for i, v in enumerate(b) if int(argv[1]) - 1 >= i), end="")
    else:
        for i in b:
            print(i, end="")
