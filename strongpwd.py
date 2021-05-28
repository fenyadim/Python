#! python3

import sys
import re
import logging

pwd = input()

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Начало программы')


def strongPwd(password):
    print('Ответ: ')
    isStrongPwd = re.compile(r'''(
      ([A-Z]+.+\d+)|
      ([A-Z]+\d+.+)|
      (.+[A-Z]+.*\d+)|
      (.+\d+[A-Z]+.*)|
      (\d+.+[A-Z]+.*)|
      (\d+.+[A-Z]+.*)
      )''', re.VERBOSE)
    match = isStrongPwd.search(password)
    if len(password) < 8:
        print('Короткий пароль')
    elif match == None:
        print('Нет верхнего регистра или нижнего или цифр')
    else:
        print(match.group() + ' - сложный пароль')


strongPwd(pwd)

logging.debug('Конец программы')
