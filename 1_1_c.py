# перевод секунд в часы, минуты и секунды
duration = int(input('Ведите количество секунд: '))
# в одном часу 3600 секунд
hours = duration // 3600
minutes = (duration//60) % 60
seconds = duration % 60
print('Результат: ' + str(hours) + ' час., ' + str(minutes) + ' мин.' + ' и ' + str(seconds) + ' сек.')
