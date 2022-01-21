prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for element in prices:
    rubles = int(element)
    kopeeks = (element - rubles) * 100
    kopeeks = round(kopeeks)
    print(f'{rubles} руб {kopeeks:02} коп')

print('-' * 50)

print(f'id списка перед сортировкой {id(prices)}')
prices.sort()
print(prices)
print(f'id списка после сортировки {id(prices)}')

print('-' * 50)

new_prices = sorted(prices, reverse=True)
print(new_prices)

print('-' * 50)

print(new_prices[:5])
