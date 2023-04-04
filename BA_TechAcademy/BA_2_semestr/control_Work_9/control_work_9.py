"""1. Создать функцию, которая возвращает строку “Hello world!”

2. Создать функцию, которая принимает аргумент для определения длины списка, создает список из символов (любых) и возвращает список в качестве ответа

3. Создать рекурсивную функцию. Не важно какую, главное чтобы она была рекурсивной

4. Создать функцию, которая принимает аргумент (список строк) и возвращает другую функцию, которая принимает аргумент surname (строка),
 соеднияет все значения в списке с данным аргументом и возвращает в ответ новый список из строк.
 Пример: [“max”, “alice”] - первый аргумент, “potter” -> Ответ: [“max potter”, “alice potter”]

5. Изменить код так, чтобы он возвращал новый список и не менял список a
def foo(items):
    items.append(42)    # Modifies the input object

a = [0, 1, 2, 3, 4, 5, 6] # [0, ... ,9]
foo(a)
print(a)

6. Какие области видимости есть в питоне?

7. Создать функцию, которая принимает все возможные аргументы в питоне и выводит на экран

8. Создать функцию по сортировке строки. Пример: Есть строка “sdjfewijAwerf” на ответ должны получить ту же строку, но отсортированную по алфавиту

9. Возвращает ли функция что-то, если в ней нету return? Если да, то что?"""


# 1

def hello_worl():
     str_1 = 'hello world'
     return str_1

print(hello_worl())

print('\n')
#2

def numbers(numbers=[]):
    for i in range(1, 16):
        numbers.append(i)
    return numbers
print(numbers())

print('\n')

#3
def func_recursl(n):
    if n == 0:
        return 1
    else:
        return n * func_recursl(n - 1)

print(func_recursl(5))

print('\n')


#4
def name(x = 'Rasul ',b='Poter '):
    list(x)
    list(b)
    def sur_name(y = 'Abdi '):
        list(y)
        return [(x+b), (y+b)]

    return sur_name()

def_2 = name()
print(def_2)

print('\n')

#5
def foo(items):
    f = [x for x in items]
    f.append(42)
    return f  # Modifies the input object

a = [0, 1, 2, 3, 4, 5, 6] # [0, ... ,9]

foo(a)
print(a)


#6
"""Локальная область видимости
Локальная область видимости наиболее часто используется в Python. Когда мы создаем переменную в блоке кода, она будет разрешена при помощи ближайшей области видимости, или областей. 
Группирование всех этих областей известно как среда блоков кода. Другими словами, все назначения выполняются в локальной области по умолчанию. 
"""

"""Глобальная область видимости
Python содержит оператор global. Это ключевое слово Python. Оператор global объявляет переменную доступной для блока кода, следующим за оператором. 
Хотя вы и можете создать наименование, перед тем, как объявить его глобальным, я настоятельно не рекомендую этого делать"""

"""Область nonlocal
В Python 3 было добавлено новое ключевое слово под названием nonlocal. С его помощью мы можем добавлять переопределение области во внутреннюю область. 
Вы можете ознакомиться со всей необходимой на данный счет информацией в PEP 3104. Это наглядно демонстрируется в нескольких примерах"""


#7
def any(a, default='d',*args,b, delta=86,   **kwargs):
    print(a,default, delta, args, b, kwargs)
any(1,2,3,4,5 ('ras',19), x=355,delta=10,c={'v':'645'} )


#8
def sort(b):
    x=[x for x in b]
    return sorted(x)
print(sort('sfnmnma'))


#9
None










