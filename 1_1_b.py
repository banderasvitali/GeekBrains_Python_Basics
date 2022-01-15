# перевод секунд в минуты и секунды
duration = int(input('Ведите количество секунд: '))
minutes = duration // 60
seconds = duration % 60
print('Результат: ' + str(minutes) + ' мин.' + ' и ' + str(seconds) + ' сек.')
