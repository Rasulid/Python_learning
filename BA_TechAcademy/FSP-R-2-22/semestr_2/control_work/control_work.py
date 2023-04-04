"""
По 5 баллов
1. Что такое PVM (python virtual machine)?

2. Напиши список базовых переменных в питоне, их описание и отличие друг от друга

3. Какие переменные являются immutable (не изменяемые), а mutable (изменяемые) и разница между ними?

4. Сколько типов форматирования у строк? Приведи пример на каждый из них

5. В чем различие is от in

6. Какие области видимости есть в питоне?

7. Возвращает ли функция что-то, если в ней нету return? Если да, то что?

## Задачи:
По 10 баллов
1. Создать функцию, которая возвращает длину наименьшей строки

2. Написать функцию, которая принимает число (функция должна работать для чисел от 0 до 99) и возвращает её как строку на английском

Пример:
name_that_number(4)   # returns "four"
name_that_number(19)  # returns "nineteen"
name_that_number(99)  # returns "ninety nine"

3. Создай из строки "You've got that fire (fire). The flavor, the style (style)" - список,
первое значени которого хранит - первую фразу, второе - вторую фразу. Результат: ["You've got that fire (fire)", "The flavor, the style (style)"]

4. Исправь код ниже. В результате он должен создать список из 9 чисел (удалять что-то из кода нельзя)
names = []
for i in range(10):
    names.append(i + 4)
if i == 7:
    names.pop(0)

5. Создать программу, которая проверяет, находиться ли строка "John" в списке names (значения списка можно самому создать),
Если строка "John" находится в списке, вывести "John"", если нет, вывести -1

6. Содать программу, которая проверяет, есть ли в словаре ключь "race" и "age", где значение ключа "age" должно быть числом.
Если проверка прошла, вывести на экран значение "race" и "age", если нет, вывести на экран строку human.

"""


# 1. Что такое PVM (python virtual machine)?
"""
PVM преобразует байт-код Python в машинно-исполняемый код. 
Если во время этой интерпретации возникает ошибка, то преобразование останавливается с сообщением об ошибке.
"""

# 2. Напиши список базовых переменных в питоне, их описание и отличие друг от друга / 3. Какие переменные являются immutable (не изменяемые), а mutable (изменяемые) и разница между ними?
"""
mutable - int , float , str , bool , tuple
immutable - list , dict , set 
iterable - list , set , tuple , dict 
"""

"""# 4. Сколько типов форматирования у строк? Приведи пример на каждый из них

print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# позиционные аргументы
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# аргументы ключевые слова
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# смешанные аргументы
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))"""

# 5. В чем различие is от in
"""оператор is проверяет идентичность самих объектов.
Его используют, чтобы удостовериться, что переменные указывают на один и тот же объект в памяти"""
"""оператор in  проверяет данный значение / переменное внутри другого переменого , in типо мост даёт доступ внутрь другого переменного
"""

"6. Какие области видимости есть в питоне?"
"""
local
global
nonlocal
buldin
"""

"""7. Возвращает ли функция что-то, если в ней нету return? Если да, то что?
None"""

# 1. Создать функцию, которая возвращает длину наименьшей строки
"""def len_finc(a ,b ,c):
    # if len(a) > len(b) and len(b) > len(c):
    #     return c
    return min(a,b,c)
print(len_finc('The notarius BIG' , 'EAZY-E', '2Pac' ))"""


"""2. Написать функцию, которая принимает число (функция должна работать для чисел от 0 до 99) и возвращает её как строку на английском
Пример:
name_that_number(4)   # returns "four"
name_that_number(19)  # returns "nineteen"
name_that_number(99)  # returns "ninety nine"


l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
      'eighty', 'ninety']


def numberInEnglish(n):
    result = ''
    if not n:
        return 'zero'
    elif n % 100 <= 19:
        result += l1[n % 100 - 1]
    else:
        result = result + l2[n % 100 // 10 - 2] + ' ' + l1[n % 10 - 1]
    return result

print(numberInEnglish(0))
print(numberInEnglish(99))""" 

"""3. Создай из строки "You've got that fire (fire). The flavor, the style (style)" - список,
первое значени которого хранит - первую фразу, второе - вторую фразу. Результат: ["You've got that fire (fire)", "The flavor, the style (style)"]

a = "You've got that fire (fire) . The flavor, the style (style)"
print(a.split("."))"""


""" 4. Исправь код ниже. В результате он должен создать список из 9 чисел (удалять что-то из кода нельзя)
names = []
for i in range(10):
    names.append(i + 4)
if i == 9:
    names.pop(0)
print(names)
"""

"""5. Создать программу, которая проверяет, находиться ли строка "John" в списке names (значения списка можно самому создать),
Если строка "John" находится в списке, вывести "John"", если нет, вывести -1

a = "John in my home"
if "John" in a :
    print("John")
else:
    print(-1)
"""

"""6. Содать программу, которая проверяет, есть ли в словаре ключь "race" и "age", где значение ключа "age" должно быть числом.
Если проверка прошла, вывести на экран значение "race" и "age", если нет, вывести на экран строку human.

s = {'rase':45,
     'age':50}
if 'race' and 'age' in s:
    print('rase','age')
else:
    print('human')"""