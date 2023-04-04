import csv
import re

"""
Дз 
1. Создать класс с атрибутами: name, email, password, purchases (список), card 
методами: 
- purchase - метод для покупки товаров. 
    Для покупки вам нужно узнать, какой товар хочет купить человек и есть у него достаточно денег для этого. 
    Если условия верны, то человек покупает товар и с его счета снимаются деньги 
    Если товара нет в списке товаров, вывести сообщение что товара нет, если не достаточно денег,  
    то вывести сообщение что не достаточно средств. 
 
- register - создать нового пользователя и включить его в список пользователей если: 
    name - должен содержать только буквы 
    email - должен содержать @ 
    password - миинмальная длинна 6 
    card - длина ключа code была равна 16 
 
    Если все условия прошли, то создать пользователя с атрибутами и записать его данные в переменную USERS. 
 
- login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
    покупки, список купленных товаров и т.д 
    Для логина вам нужно узнать, есть ли такой пользователь в системе или нет. Если его нет, то сказать что нужно пройти регистрацию. 
    Если есть, то создать все атрибуты класса из имеющихся данных. 
 
- add_product - добавить куплейнный товар в атрибут purchases.
"""


enter_option = str(input('выберите "Регистрацыя или Логин" = '))

# class Steam:
#     purchase = {}
    # name = None
    # email = None
    # password = None
    # card = None

    # def __init__(self , enter_option):
    #     if enter_option == '1':
    #         self.register()
    #     elif enter_option == '2':
    #         self.login()

def chek_users_id():
    with open('register.csv') as register:
        content = csv.DictReader(register)
        count = 0
        for row in content:
            count += 1
    return count

def register(name = None ,email = None,password = None,card = None , user_id = None):
    name = input('напишите ваше имя = ')
    re_name = r"[a-zA-Z]+"
    name_s = re.search(re_name , name ,re.IGNORECASE)
    email = input('напишите ваш email = ')
    re_email = r"[@]"
    email_se = re.search(re_email , email , re.IGNORECASE )
    password = input('придумайте пароль = ')
    re_card = r"[\d_ @$!%*?&]{,19}"
    card =  input('ваведите реквизиты карты = ')
    user_id = user_id = chek_users_id()

    if name_s:
        name_s = name
        print(name)
    if email_se:
        email_se = email
        print(email)
    if password :
        password = password
        print(password)
    if card :
        card = card
        print(card)
    if user_id:
        user_id = user_id
        print(user_id)

    if name and email and password and card:
        with open('register.csv' , 'a' , newline='' , encoding='utf-8') as register:
            write = csv.writer(register , delimiter=',')
            # write.writerow([ 'name' , 'email' , 'password' , 'card' , 'purchase' , 'id'])
            write.writerow([ name , email , password , card  , user_id , user_id])

    
def login(email = None , password = None):
    imp_email =input("напишите email = ")
    imp_password =input("напишите пароль = ")
    re_email = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    re_email = r"[A-Za-z\d_@$!%*?&]{8,}"
    email_se = re.search(re_email , imp_email , re.IGNORECASE )
    password_se = re.search(re_email , imp_password , re.IGNORECASE )
    print(email_se)
    print(password_se)


    # if email_se:
    #     done_email = email_se
    # if password_se:
    #     done_password = password_se
    # with open('register.csv') as reg :
    #     content = csv.DictReader(reg)
    #     for row in content:
    #         if done_email in row and done_password in row:
    #             print('loged!' , row)


                    
# print(register())
print(login())

# steam = Steam(enter_option=enter_option)

# name = input('напишите ваше имя = ')
# re_name = r"[a-zA-Z]+"
# name_s = re.search(re_name , name ,re.IGNORECASE)
# print(name_s)












        