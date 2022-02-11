import re


def email_parse(email_addr):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_addr):
        raise ValueError(f'wrong email: {email_addr}')
    print(re_email.match(email_addr).groupdict())


for i in ['someone@geekbrains.ru', 'som&one@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as error:
        print(error)
