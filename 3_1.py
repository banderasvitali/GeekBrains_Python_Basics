def num_translate(word):
    translate = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'siх': 'шесть',
        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }
    result = translate.get(word)
    if not word:
        return 'None'
    else:
        return result


#Для проверки
print(num_translate('one'))
