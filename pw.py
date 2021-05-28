# ! python3
# pw.py - Программа для незащищенного хранения паролей.

import pyperclip
import sys
PASSWORD = {'email': '1234567890',
            'blog': '1234554321',
            'luggage': '123'}


if len(sys.argv) < 2:
    print(
        'Использование: python pw.py [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Пароль для ' + account + ' скопирован в буфер.')
else:
    print('Пароль для ' + account + ' нет в списке.')
