src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
numbers = set()
for i in src:
    if i not in numbers:
        unique.add(i)
    else:
        unique.discard(i)
    numbers.add(i)
unique_from_src = [i for i in src if i in unique]
print(unique_from_src)
