def num_translate_adv(word):
    translate = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'siх': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }
    result = translate.get(word.lower())
    if result:
        if word.istitle():
            return result.title()
        return result
    else:
        return 'None'


#Для проверки
print(num_translate_adv('One'))
