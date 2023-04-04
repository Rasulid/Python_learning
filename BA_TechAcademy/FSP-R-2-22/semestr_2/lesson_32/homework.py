"""
STEAM - APP





Я переписал условие и надеюсь задание станет более понятным для вас

Задание.
К вам пришел заказчик и сказал что он хочет онлайн магазин и дал список требований.
Требования:
1. Система должна поддерживать функцию регистрации и логина
2. Позволять покупать любой продукт в базе данных
3. Вычесть деньги из карты пользователя

Мы можем решить эту задачу двумя способами:
1. Создать класс
2. Создать кучу функций

Мы знаем, что работать с классами лучше, так как классы изолированные, поддерживают наследство, хороши для описания объектов

Первым делом нам нужно создать класс и определиться с атрибутами, которые мы будем использовать и
создать методы по требованию заказчика, так же нам нужна база данных, для этого мы будем использовать файлы типа CSV

Техническое Описание Задания для классов:
1. Создать класс с атрибутами name, email, password, purchases (список), card
    name (str) - это реальное имя пользователя, Которое должно состоять только из букв
    email (str) - у мейла есть несколько требований: (строка)@(строка).(2 или более букв)
        Регулярное выражение для email: ([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+
    password (str) - требования для пароля:
        1. минимум 6 символов
        2. Должен содержать буквы, цифры
        3. Должен содержать одну большую букву
    purchases - пустой список для хранения купленных товаров (необязательно использовать список)
    card - словарь из двух ключей: code (str) - 16 чисел, balance (int) - баланс на счету
2. Создать методы класса по требования заказчика:
    register - регистрация юзера. Так как мы работаем с классами, создание юзера это тоже самое что и создать
    экземпляр класса. Для этого нужно убедиться что все данные пользователя правильные. Условия к данным пользователя выше.
    Перед созданием пользователя нужно убедиться, что его нету в списке пользователей (для этого у вас должен быть файл,
    где вы храните уже созданных пользователей). Если такой пользователь уже есть, то вывести ошибку, что пользователь не создан.
    login - Вход в систему с помощью email и password, если пользователь с такими данными уже есть.
    purchase - делает покупку товара для пользователя. Для этого нужно узнать, есть ли этот товар в наличии (файл, где вы храните
    названия и цену продуктов). Если товар есть и у покупателя есть достаточно денег на счету -> купить товар, вычест деньги из счета
    пользователя и добавить товар в атрибут purchases и файл.
    add_product - метод для добавления купленного товара в файл и атрибут purchase пользователя.

Доп.
Создать метод по удалению пользователя. При этом данные о нем должны удалиться из всех файлов.
"""

import csv
import re

NAME_PATTERN = r"[a-zA-Z]"
EMAIL_PATTERN = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
PASSWORD_PATTERN = r'[A-Za-z0-9@#$%^&+=]{8,}'
CARDCODE_PATTERN = r"\d{16}"


class Steam:
    purchases = []
    card = {
        'code': " ",
        'balance': None,
    }

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card['code'] = card_code
        self.card['balance'] = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        with open('users.csv', encoding='utf-8') as users:
            result = csv.DictReader(users)

            for row in result:
                if row['email'] == email and row['password']:
                    return 'User with this email is already exist'
                elif row['email'] != email and row['password']:

                    continue

        if re.search(NAME_PATTERN, name) and re.search(EMAIL_PATTERN, email) and re.search(PASSWORD_PATTERN, password) \
                and re.search(CARDCODE_PATTERN, card_code):
            with open('users.csv', 'a', newline='', encoding='utf-8') as users:
                writer = csv.writer(users, delimiter=',')
                writer.writerow([name, email, password, card_code, card_balance])

            return cls(name, email, password, card_code, card_balance)

        else:
            return 'Wrong credentials'

    @classmethod
    def login(cls, email_l, password_l):
        if re.search(EMAIL_PATTERN, email_l) and re.search(PASSWORD_PATTERN, password_l):
            with open('users.csv', encoding='utf-8') as login:
                result = csv.DictReader(login)

                for row in result:
                    print(row)
                    if row['email'] == email_l and row['password']:
                        print('logging is success')
                        continue

                    elif row['email'] != email_l and row['password']:
                        print('you are note in data base , please go to the registration')

                    else:
                        print("your code is doesn't works")

    def purchase(self):
        pass

    def add_product(self):
        pass


def run_steam():
    print(Steam.card)

    register = input('choose the operation "Registration or Login" = ')

    if register == '1':
        name = str(input('Enter your name = '))
        email = str(input('enter your email = '))
        password = input('create password = ')
        card_code = input('enter your card code = ')
        card_balance = int(input('card balance = '))
        user_1 = Steam.register(name=name, email=email, password=password, card_code=card_code, card_balance=card_balance)
        print(user_1)
        print(Steam.card)

    elif register == '2':
        email_l = str(input('enter your email = '))
        password_l = input('enter password = ')
        user = Steam.login(email_l=email_l, password_l=password_l)
        print(user)
    else:
        print('Wrong logging')


print(run_steam())
