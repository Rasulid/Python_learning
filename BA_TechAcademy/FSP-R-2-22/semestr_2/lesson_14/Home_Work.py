#
# """
# Создать класс, описывающий персонажа/игрока с переменными:
# username, email, password, health, abilities, specialization, items (можно создать еще)
# У класса должно быть три метода:
# """
#
# """Войти в игру:
# если пароль и логин правильные,
# то вернуть в ответ сообщение об удачном логине,
# если не правильные - об обратном"""
#
# """
# Дать пользователю возможность выбора специализации. Специализации создайте сами. Пример: (рыцарь, гта персонаж, и что-то ещё)
# 3. После выбора персонажа, у него должен создаться персонаж с начальными параметрами. Пример
# health=100
# specialization=assassin
# abilities=(список возможностей)
# items=(список вещей которые у него есть)
# """
#
# users_name = str(input('Enter your username = '))
# users_email = str(input('Enter your Email = '))
# users_pass = str(input('Enter your password = '))
#
# if users_name == "Rasul":
#     print('Welcome to system')
# elif users_name != "Rasul":
#     print("Excuse me your username is not defined. \nPlease check your username ;)")
#
#
# if users_email == "123rasul":
#     print('Welcome to system')
# elif users_name != "123rasul":
#     print("Excuse me your Email is not defined. \nPlease check your Email ;)")
#
# if users_pass == "1234":
#     print('Welcome to system')
# elif users_name != "1234":
#     print("Excuse me your password is not defined. \nPlease check your password ;)")
#
# class PersonalAtribute:
#
#     """
#     first method - is need to registration
#     second method - is comments need to in the game
#     third method - is something items to need
#     """
#
#     def __init__(self , username , email , password):
#         self.username = username
#         self.email = email
#         self.password = password
#
#     def personaje(self , someone):
#         self.someone = someone
#
#     def in_game(self , health , abilities , specialization):
#         self.health = health
#         self.abilities = abilities
#         self.specialization = specialization
#
#     def something(self , items):
#         self.items = items
#
#
# calling_class = PersonalAtribute(users_name , users_email , users_pass)
# gamig_personaje =calling_class.personaje()

import pygame
pygame.init()