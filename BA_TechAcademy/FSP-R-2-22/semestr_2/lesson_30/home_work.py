import csv
"""
Дз
1. Создать класс с атрибутами: name, email, password, purchases (список), games (список), card и методами:

- purchase метод по покупке игры, если она платная. У вас должен быть некий список игр в вашей системе, который храниться в csv файле.
Поля для файла сами выберите

- register регистрация юзера, если его нету. При этом вам нужно проверить, есть ли такой юзер в системе.
Для этого можете создать файл, который хранит данные о пользователе и выберите уникальное поле.
Уникальное поле - это какой-то из атрибутов класса. Можете выбрать email или создать поле id, которое будет увеличиваться при добавлении нового пользователя

- login вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные: покупки, список игр и т.д

- add_game - добавить игру в список игр. Но при этом учтите, что игра может быть платной.

Это по сути steam или любой игровой лаунчер, но проще.

Доп.
Создать метод по удалению пользователя. При этом данные о нем должны удалиться из всех файлов

"""

class Steam:
    def __int__(self , name , email , password , purchases , games , card ):
        self.name = name
        self.email = email
        self.password = password
        self.purchases = purchases
        self.games = games
        self.card = card

    def purchase(self):  #покупки
        with open('purchase.csv' ,'w' , newline='' , encoding='utf-8') as pur:
            write = csv.writer(pur , delimiter=',')
            write.writerow(['name' , 'size' , 'type' , 'prise'])
            write.writerow(['warfame' , '32GB' , 'shuter' , '12$' ])
            write.writerow(['need for speed' , '320GB' , 'racing' , '113$' ])
            write.writerow(['dote 3' , '92GB' , 'strateg' , '80$' ])
            write.writerow(['pubg' , '132GB' , 'shuter' , '120$' ])


    def register(self):
        with open('register_id.csv', 'w',newline='' ,encoding='utf-8') as id:
            write = csv.writer(id , delimiter=',')
            write.writerow(['name' , 'username' , 'email' , 'id' ])
            write.writerow(['rr' , 'RR' , 'RR@gmail.com' , '0001' ])
            write.writerow(['mm' , 'MM' , 'MM@gmail.com' , '0002' ])
            write.writerow(['ss' , 'SS' , 'SS@gmail.com' , '0003' ])
            write.writerow(['dd' , 'DD' , 'DD@gmail.com' , '0004' ])
            # reader = csv.DictReader(id)
            # for row in reader:
            #     if 'RR' in row:
            #         print('Есть')
            #         break
            #     else:
            #         print('Нет')

    # def login(self):
    #     with open('login.csv', 'w',newline='' ,encoding='utf-8') as log :
    #         write = csv.writer()

    def add_game(self):
        with open("p.csv" ,'w' ,newline='' ,encoding='utf-8') as game:
            write = csv.writer(game, delimiter=',')
            write.writerow(['name' , 'size' , 'type' , 'prise'])
            write.writerow(['warfame' , '32GB' , 'shuter' , '12$' ])
            write.writerow(['need for speed' , '320GB' , 'racing' , '113$' ])
            write.writerow(['dote 3' , '92GB' , 'strateg' , '80$' ])
            write.writerow(['pubg' , '132GB' , 'shuter' , '120$' ])
            


steam = Steam()
steam.purchase()
steam.register()
# steam.login()
steam.add_game()

# сделал как смог(