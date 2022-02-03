from collections import Counter

with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    my_dict = Counter()
    for i in f:
        my_dict[i.split()[0]] += 1

    ip = my_dict.most_common(1)[0][0]
    times = my_dict.most_common(1)[0][1]
    print('Spammer IP','-', ip, '-', times, 'times')
