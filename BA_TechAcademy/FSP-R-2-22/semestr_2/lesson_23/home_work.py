"""
Дз
1. Решить три кодварса любой сложности, которую вы осилите (можно 8, 7, 6 кью или даже 5 и сложнее)

2. Создать декоратор, который запускает функцию только в дневное время (от 7 утра до 10 вечера), 
если время позднее, то не запускать функцию

3. Создать декоратор, который выводит на экран информацию о функции.
Пример:
def make_greeting(name, age=None): 
    if age is None: 
        return f"Howdy {name}!" 
    else: 
        return f"Whoa {name}! {age} already, you are growing up!"

Ответ после вызова функции выше с помощью одного и двух аргументов:
С одним аргументом
Calling make_greeting('Coronel') 
'make_greeting' returned 'Howdy Coronel!' 

С двумя аргументами
Calling make_greeting('Coronel', age=20) 
'make_greeting' returned 'Whoa Coronel! 20 already, you are growing up!'
"""




# def t_dec(func):
#     def wrapper(n):
#         print(func(n))
#         if n <= 6 : 
#             print('function is not working')

#         elif n >= 22:
#             print('function is not working')

#         else :
#             print("function is working")
#     return wrapper


# @t_dec
# def imp_time(time):
#     print(time)

# imp_time(10)


import functools
def debug(func):
    @functools.wraps(func)
    def wrapp_debug(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k , v in kwargs.items()]
        print(args_repr , kwargs_repr , sep='\n')
        signature = " , ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args , **kwargs)
        print(f"{func.__name__!r} retuned {value!r}")
        return value
        
    return wrapp_debug  

@debug
def make_greeting(name, age=None): 
    if age is None: 
        return f"Howdy {name}!"
    else: 
        return f"Whoa {name}! {age} already, you are growing up!"

print(make_greeting('Rasul',19))

# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# l = [1,2,'aasf','1','123',123]
# sorted_int = []
# for x in l:
#     if type(x) != str:
#         sorted_int.append(x)
# print(sorted_int)

# https://www.codewars.com/kata/523f5d21c841566fde000009
# def array_diff(a, b):
#     return [x for x in a if x not in set(b)]

# print(array_diff([1,2], [1]))
# print(array_diff([1,2,3], [1, 2]))


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))