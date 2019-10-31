# Ввести почтовый адрес. Проверить доменной имя. В случае если оно gmail.com,
# вывести на экран имя почтового ящика. Иначе вывести надпись “DOMAIN NAME is not supported’

email = input('Enter e-mail --->')
split_email = email.split('@')
domain = split_email[1]
if domain == 'gmail.com':
    print(email)
else:
    print('DOMAIN NAME is not supported')
