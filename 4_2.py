from requests import get, utils


def currency_rate(currency_code):
    responce = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(responce.headers)
    content = responce.content.decode(encoding=encodings)

    for i in content.split('<CharCode>')[1:]:
        code = i[:3]
        result = (i.split('<Value>')[1:][0].split('</Value>')[0])
        result = result.replace(',', '.')
        result = float(f'{float(result):.2f}')

        if currency_code.upper() == code:
            return f'курс {code}: {result} руб'


print(currency_rate('usd'))
