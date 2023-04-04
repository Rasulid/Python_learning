"""

    гит
        как фиксировать изменение
        цикл коммита
        гитигнор
        merge конфликт
        pull request

"""



"""
Базовый питон:

    переменные
    итерируемые перменные
    методы переменных
    условия
    циклы
    функции
    ключевое слово return
    аргументы с функциями
    области видимости
    вложенные функции
    рекурсия

    гит
        как фиксировать изменение
        цикл коммита
        гитигнор
        merge конфликт
        pull request
    классы

        создание класса
        init
        метода класса
        атрибуты класса
        инкапсуляция
        приватные и публичные переменные
        полиморфизм
        наследование
        super
        MRO
        operator/method overloading

    декораторов
    как вызывать декоратор без @
    как создавать полноценный декоратор
    как в декораторе принимать аргменты
    исключения
    итераторов
    что такое next
    функции высшего порядка
    comprehension
    файлы
    csv файлы
    регулярные выражения
    тестирование


"""

# ________________________________________________________________________________________________________________________
"""
1
imutble 
    
    int 
    float
    complex
    bool
    tuple
    str
    frozenset
mutble
    list
    set
    dict
    
itrble 
    list
    dict
    tuple
    set
    https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html#:~:text=An%20iterable%20is%20any%20Python,over%20in%20a%20for%2Dloop.
"""
# ________________________________________________________________________________________________________________________

"""    методы переменных   """

# https://www.w3schools.com/python/python_ref_string.asp  string
# https://www.w3schools.com/python/python_ref_list.asp   list
# https://www.w3schools.com/python/python_ref_dictionary.asp   dict
# https://www.w3schools.com/python/python_ref_tuple.asp   tuple
# https://www.w3schools.com/python/python_ref_set.asp  set

# ________________________________________________________________________________________________________________________

"""    условия (if - else - elif) """

x = int(input())
if x > 0:
    print(x)
else:
    print(-x)

# ________________________________________________________________________________________________________________________

"""    циклы (while , for)"""

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print()

"твблица умножения"

"""
1       2       3       4       5       6       7       8       9
2       4       6       8       10      12      14      16      18
3       6       9       12      15      18      21      24      27
4       8       12      16      20      24      28      32      36
5       10      15      20      25      30      35      40      45
6       12      18      24      30      36      42      48      54
7       14      21      28      35      42      49      56      63
8       16      24      32      40      48      56      64      72
9       18      27      36      45      54      63      72      81   
"""
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, '*', j, '=', i * j, end='\t')
        j += 1
    i += 1
    print()

"""
1 * 1 = 1       1 * 2 = 2       1 * 3 = 3       1 * 4 = 4       1 * 5 = 5       1 * 6 = 6       1 * 7 = 7       1 * 8 = 8       1 * 9 = 9
2 * 1 = 2       2 * 2 = 4       2 * 3 = 6       2 * 4 = 8       2 * 5 = 10      2 * 6 = 12      2 * 7 = 14      2 * 8 = 16      2 * 9 = 18
3 * 1 = 3       3 * 2 = 6       3 * 3 = 9       3 * 4 = 12      3 * 5 = 15      3 * 6 = 18      3 * 7 = 21      3 * 8 = 24      3 * 9 = 27
4 * 1 = 4       4 * 2 = 8       4 * 3 = 12      4 * 4 = 16      4 * 5 = 20      4 * 6 = 24      4 * 7 = 28      4 * 8 = 32      4 * 9 = 36
5 * 1 = 5       5 * 2 = 10      5 * 3 = 15      5 * 4 = 20      5 * 5 = 25      5 * 6 = 30      5 * 7 = 35      5 * 8 = 40      5 * 9 = 45
6 * 1 = 6       6 * 2 = 12      6 * 3 = 18      6 * 4 = 24      6 * 5 = 30      6 * 6 = 36      6 * 7 = 42      6 * 8 = 48      6 * 9 = 54
7 * 1 = 7       7 * 2 = 14      7 * 3 = 21      7 * 4 = 28      7 * 5 = 35      7 * 6 = 42      7 * 7 = 49      7 * 8 = 56      7 * 9 = 63
8 * 1 = 8       8 * 2 = 16      8 * 3 = 24      8 * 4 = 32      8 * 5 = 40      8 * 6 = 48      8 * 7 = 56      8 * 8 = 64      8 * 9 = 72
9 * 1 = 9       9 * 2 = 18      9 * 3 = 27      9 * 4 = 36      9 * 5 = 45      9 * 6 = 54      9 * 7 = 63      9 * 8 = 72      9 * 9 = 81
"""
# ________________________________________________________________________________________________________________________

"    функции"


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# ________________________________________________________________________________________________________________________

"    ключевое слово return"


def my_function(child3, child2, child1):
    return "The youngest child is " + child3


print(my_function(child1="Emil", child2="Tobias", child3="Linus"))

# ________________________________________________________________________________________________________________________
"    аргументы с функциями"


def func(a, b="Abduvaitov", *args, **kwargs):
    return a, b, args, kwargs


print(func('Rasul', ['R', 'A', 'S', 'U', 'L'], {'key': 'value'}))

# ________________________________________________________________________________________________________________________
"    области видимости"

candy = 5


def get_candy():
    global candy
    candy += 1
    print('У меня {} конфет.'.format(candy))


get_candy()
get_candy()
print(candy)

# global
# locale
# nonlocal
# building
# ________________________________________________________________________________________________________________________

'    вложенные функции'


def func(i):
    def func_2():
        print(f'hello {i}')

    return func_2()


print()
# ________________________________________________________________________________________________________________________

"    рекурсия "
count = 0
def short_story():
    print("У попа была собака, он ее любил.")
    print("Она съела кусок мяса, он ее убил,")
    print("В землю закопал и надпись написал:")
    global count
    count += 1
    if count == 8:
        print(count)
        return count
    short_story()
short_story()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# ________________________________________________________________________________________________________________________

"""
    классы

        создание класса
        init
        метода класса
        атрибуты класса
        инкапсуляция
        приватные и публичные переменные
        полиморфизм
        наследование
        super
        MRO
        operator/method overloading
"""


class Test:
    atriboots = 78
    def __init__(self , name , surname , age):
        self.name = name
        self.surname = surname
        self.age = age

    def _private(self):
        repr("Это приватный метод!")

    def __private(self):
        print("Это приватный метод!")


t = Test(45 , 345 , 23)
print(t._Test__private())
print(t._private)


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)
#https://www.geeksforgeeks.org/python-super/


# class A:
#     pass
#
#
# class B:
#     pass
#
#
# class C(A, B):
#     pass
#
#
# class D(B, A):
#     pass
#
#
# class E(C, D):
#     pass

# print(E.mro())

#https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/

# ________________________________________________________________________________________________________________________


"""
 декораторов
    как вызывать декоратор без @
    как создавать полноценный декоратор
    как в декораторе принимать аргменты
    исключения
    итераторов
    что такое next
    функции высшего порядка
    comprehension
    файлы
    csv файлы
    регулярные выражения
    тестирование
"""
from time import time
def my_decorator(func):
    def wrapper(n):
        start = time()
        print('result 1 = ' ,func(n))
        print('result 2 = ' ,func(n))
        end = time()
        return f'time for working {end - start}'
    return wrapper

def factorial(n):
    if n < 0:
        return 1
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    return fact

dec =my_decorator(factorial)(10)
print(dec)


def add_mark(**kwargs):
    def decorator(func):
        for key, value in kwargs.items():
            setattr(func, key, value)
        return func
    return decorator


@add_mark(test=True, ordered=True)
def test_function(a, b):
    return a + b

print(test_function(123 , 1324))


f = open('1.txt' , mode='w')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print('Это что ещё такое?')
else:
    print('Всё хорошо.')
finally:
    f.close()
    print('Я закрыл файл.')

"""
Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз.
С точки зрения Python - это любой объект, у которого есть метод __next__ .
Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration,
когда элементы закончились.
"""


"""
Функция высшего порядка – это функция, которая может принимать в качестве аргумента другую функцию и/или 
возвращать функцию как результат работы
"""


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
comprehension = [x for x in fruits if 'a' in x ]
print(comprehension)

import csv

with open('test_file.csv' , 'w' , encoding='utf-8' , newline='') as test:
    write = csv.writer(test , delimiter=',')
    write.writerow(["apple", "banana", "cherry", "kiwi", "mango"])



#ReGix
#https://regex101.com/r/sG1qP1/533



def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

print(infinite_sequence())


"""
итераторы 
Декоратор 
Генератор 
Тестирования
"""


'merge konflict' #https://www.youtube.com/watch?v=sMLazIg9xIY


