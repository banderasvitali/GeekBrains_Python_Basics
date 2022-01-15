# перевод секунд в дни, часы, минуты и секунды
duration = int(input('Ведите количество секунд: '))
# в одном дне 86400 секунд
days = duration // 86400
hours = (duration//3600) % 24
minutes = (duration//60) % 60
seconds = duration % 60
print('Результат: ' + str(days) + ' дн., ' + str(hours) + ' час., ' + str(minutes) + ' мин.' + ' и ' + str(seconds) + ' сек.')
