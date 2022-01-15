new_list = []
total_sum = 0
for i in range(1, 1001):
    if i % 2 != 0:
        new_list.append(i**3 + 17)
for n in new_list:
    number = n
    sum_number = 0
    while n > 0:
        end_number = n % 10
        n = n // 10
        sum_number += end_number
    if sum_number % 7 == 0:
        total_sum += number
print(total_sum)
