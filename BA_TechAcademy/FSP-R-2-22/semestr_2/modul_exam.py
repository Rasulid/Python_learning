import csv
"Теория"
"""
1 "
None (неопределенное значение переменной)
Логические переменные (Boolean Type)
Числа (Numeric Type)
    int – целое число
    float – число с плавающей точкой
    complex – комплексное число
Списки (Sequence Type)
    list – список
    tuple – кортеж  
    range – диапазон
Строки (Text Sequence Type )
    str
Бинарные списки (Binary Sequence Types)
    bytes – байты
    bytearray – массивы байт
memoryview – специальные объекты для доступа к внутренним данным объекта через protocol buffer
Множества (Set Types)
    set – множество
    frozenset – неизменяемое множество
Словари (Mapping Types)
    dict – словарь
"


2"

str и  int
"

3 "

Погорим о наследовании. Если один класс унаследован от другого, то он от него перенимает себе методы и атрибуты своего родителя. Вы, конечно, можете переопределить некоторые из них или добавить свою новую функциональность – в этом и есть смысл наследования.
"

4"
git add .  ->  git commit -m " " -> git push
"

5"
Декораторы - важная часть Python. Если коротко: они являются функциями, которые изменяют работу других функций. Они помогают делать код короче и более "питонистичным". Большинство новичков не знает, где их использовать, так что я расскажу о нескольких случаях, когда декораторы помогут написать лаконичный код.
"
"""



"Теория + Задачи"
"""
1 Перечислите и Приведите пример оператов: сравнения, логических, особые операторы

== , > , < , >= , <= , !=
True , False , end , or , is , in
+ , - , * , / , // , % , **
"""

"""
2 Можно ли вызвать декоратор без @, если да, то приведите пример
да 


def decorator(func):
    def wrapper(n):
        pass
    return wrapper
    
def func(n):
    pass
    
print(decorator(func)(value))
"""

"""
3.Исправьте код. В конце вы должны создать код по проверке данных ползователя и возвращает сообщение об успешном или проваленном логине.
def validate(username, password):
    username "Random" password 2321ewfsef
    return "Вы успешно вошли в систему!"
    return Пароль или имя пользователя не правильны
"""


def validate(username, password):
    if username == "Random" and password == '2321ewfsef':
        return "Вы успешно вошли в систему!"
    else:
        return "Пароль или имя пользователя не правильны"


"""4 Приведете список областей видимости в питоне и пример с каждым из них."""

"""global 
locale
nonlocal
"""

b = 'global'


def test():
    s = 'local'


def myfunc1():
    x = "John"

    def myfunc2():
        nonlocal x
        x = "hello"

    myfunc2()
    return x


"""5 Напишите шаблон декоратора который может принимать аргументы """


def deley(something):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    return decorator


# _______________________________________________________________________________________________________________________

" Задачи "
"""1  Создать функцию генератор по нахождению чисел фиббоначи"""

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

# print(list(fib(10)))


""" 2 Создать класс Gum, который описывает жевачку с атрибутами: smell, price, company, name, special_features, count и с методом str, 
который возвращает информацию о жевачке со всеми атрибутами. От класса Gum создать два других класса: Orbit и Trident. 
Orbit должен иметь ещё один атрибут country (страна произвдства). Trident должен иметь ещё один атрибут date_of_production (дата производства).
taste - вкус
price - цена
company - производившая компания 
name - имя 
special_features - имеет вкус арбуза, лимона и т.д.
count - количество в упаковке """


class Gum:
    def __init__(self , smell, price, company, name, special_features, count):
        self.smell = smell
        self.price = price
        self.company = company
        self.name = name
        self.special_features = special_features
        self.count = str(count)

    def __str__(self):
        return f' smell {self.smell} , price {self.price} , company {self.company} , name  {self.name} , special features {self.special_features} , count {self.count}'

class Orbit(Gum):
    def __init__(self, smell, price, company, name, special_features, count , county):
        super(Orbit, self).__init__(smell, price, company, name, special_features, count)
        self.country = county


class Trident(Gum):
    def __init__(self , smell, price, company, name, special_features, count ,date_of_production):
        super(Trident, self).__init__(smell, price, company, name, special_features, count)
        self.date_of_production = date_of_production

trid = Trident('merllon' , 12 , 'Trident' , 'Trident' ,'имеет вкус арбуза, лимона и т.д.' , "20"  , 20)
# print(trid.__str__())


"""


def sum(a):
    sum = 0
    for i in a:
        sum += i
    return sum

def is_defended(attackers, defenders):
    final = len(defenders) - len(attackers)
    for i in range(len(attackers)):
        try:
            if attackers[i] > defenders[i]:
                final -= 1
            else:
                final += 1
        except:
            break
            
    if final == 0:
        return sum(attackers) <= sum(defenders)
    
    return False if final < 0 else True
    
#https://www.codewars.com/users/R%2FA/completed_solutions
"""


"""
Сейчас стало модно использовать двух-уровневую аутентификацию. 
Что это такое? Это когда человек проходит двойную проверку. Сперва черех обычный экран ввода пароли и имени пользователя, второе через код, 
который доставляется в мейл или через стороннее приложение. Создать функцию, которая делает схожие действия. 
После успешного входа в систему, вы должны сказать пользователю, что ему нужно пройти ещё одну проверку для полноценного входа в виде 4 значного числа (2342). 
Так как мы ещё не прошли как отправлять сообщения в мейл, вам нужно сделать это через файлы. 
В момент когда вы проходите второй вход, вам нужно записать в файл с названием (random_code.txt или csv) 4 значное число, которое нужно ввести, 
чтобы войти в систему и вывести сообщение об успешном входе. Пример успешной работы:

Чтобы войти в систему введите пароль и имя пользователя
Имя пользователя: 
Пароль: 
Ура! Вы вошли в систему, но вам нужно подтвердить что это вы черезз код. Мы отправили его вам в файл random_code.txt.
Введиет пароль: 
Верно имя_пользователя! Вы успешно вошли в систему.


"""
EMAIL = 'rasulabduvaitov@gmail.com'
PASSWORD = '1234rasulaka'
COUNT = 0000

def registration(email, password, count=COUNT):
    email = str(input("entter your emaiil = "))
    password = input("enter your password = ")
    if email == EMAIL and password == PASSWORD:
        count += 1
        print('Ура! Вы вошли в систему, но вам нужно подтвердить что это вы черезз код. Мы отправили его вам в файл random_code.csv.')

        with open('random_code.csv' , 'w' , newline='' , encoding='utf-8') as random :
            write = csv.writer(random , delimiter=',')
            write.writerow([count])

        input_count = input('потвердите пароль , посмотрите  = ')
        if input_count == count:
            print('добро пожаловать в систему :)')
        else :
            print('неправильноо зайдите заново !!!')
            return 'неправильноо зайдите заново !!!'

    else:
        return 'неправильноо зайдите заново !!! '

# registration(EMAIL , PASSWORD)

"""
declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
Lew attacks Harry; Harry now has 3 health.
Harry attacks Lew; Lew now has 6 health.
Lew attacks Harry; Harry now has 1 health.
Harry attacks Lew; Lew now has 2 health.
Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
"""


class Fighter(object): 
    def __init__(self, name, health, damage_per_attack): 
        self.name = name 
        self.health = health 
        self.damage_per_attack = damage_per_attack 
 
fighter_1 = Fighter("Lew", 10, 2) 
fighter_2 = Fighter("Harry", 10, 2) 
 
# Typing 
def declare_winner(fighter_1: Fighter, fighter_2: Fighter, winner: str): 
    while True: 
        if winner == 'Harry':
            fighter_2.health -= fighter_1.damage_per_attack # 8 6 4 2 0 
            fighter_1.health -= fighter_2.damage_per_attack # 8 6 4 2 0 
            print("1", fighter_1.health, "2", fighter_2.health) 
            if fighter_2.health < 0: 
                return f"{fighter_1.name} attacks {fighter_2.name}:{fighter_2.name} now has -1 health and is dead. {fighter_1.name} wins." 
            if fighter_1.health < 0: 
                return f"{fighter_2.name} attacks {fighter_1.name}:{fighter_1.name} now has -1 health and is dead. {fighter_2.name} wins." 
            print(f'{fighter_1.name} attacks {fighter_2.name}; {fighter_2.name} now has {fighter_2.health}.') 
            print(f'{fighter_2.name} attacks {fighter_1.name}; {fighter_1.name} now has {fighter_1.health}.') 

        if winner == 'Lew':
            fighter_1.health -= fighter_2.damage_per_attack # 8 6 4 2 0 
            fighter_2.health -= fighter_1.damage_per_attack # 8 6 4 2 0 
            print("1", fighter_1.health, "2", fighter_2.health) 
            if fighter_2.health < 0: 
                return f"{fighter_1.name} attacks {fighter_2.name}:{fighter_2.name} now has -1 health and is dead. {fighter_1.name} wins." 
            if fighter_1.health < 0: 
                return f"{fighter_2.name} attacks {fighter_1.name}:{fighter_1.name} now has -1 health and is dead. {fighter_2.name} wins." 
            print(f'{fighter_1.name} attacks {fighter_2.name}; {fighter_2.name} now has {fighter_2.health}.') 
            print(f'{fighter_2.name} attacks {fighter_1.name}; {fighter_1.name} now has {fighter_1.health}.') 
 
print(declare_winner(fighter_1, fighter_2, "Harry")) # => "Lew"