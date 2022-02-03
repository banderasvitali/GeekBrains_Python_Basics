from itertools import  zip_longest

with open("users.csv", "r", encoding="utf-8") as users:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        join_list = zip_longest(users, hobby, fillvalue=None)

        with open("new_list.txt", "w", encoding="utf-8") as f:
            for i in join_list:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)