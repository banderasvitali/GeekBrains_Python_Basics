from requests import get, utils
from datetime import datetime


def currency_rate(currency_code):
    responce = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(responce.headers)
    content = responce.content.decode(encoding=encodings)
    data_time = content.split('Date="')[1][:10].split('.')
    data_time = datetime(day=int(data_time[0]), month=int(data_time[1]), year=int(data_time[2])).date()

    for i in content.split('<CharCode>')[1:]:
        code = i[:3]
        result = (i.split('<Value>')[1:][0].split('</Value>')[0])
        result = result.replace(',', '.')
        result = float(f'{float(result):.2f}')

        if currency_code.upper() == code:
            return f'{data_time}: курс {code}: {result} руб'


print(currency_rate('EUR'))

