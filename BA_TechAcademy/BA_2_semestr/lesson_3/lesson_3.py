# def function (argument):
#     argument = 'Hello World!'
#     print(argument)

# function(argument='')

# def func_name(a):
#     print(type(a),a)

# func_name('123')
# func_name(123)
# func_name([1,2,3])
# func_name({1,2,3})
# func_name({1:1,2:2,3:3})

# def func_args (a , b, c):
#     print(type(a) , type(b) , type(c))

# func_args((2,5) , '5' , True)

# def ex_s (lenght , number):
#     numbers = []
#     for i in range(lenght + 1):
#         numbers.append(i * number)
#     return numbers

# x = ex_s(10 , 3)
# print(x)
# print(ex_s(5 , 5))


"""1. Понять что от меня требуется 
2. Создаю шаги для выполнения 
    2.1 Создать бесконечный цикл 
    2.2 Создать генератор букв и символа " " (пробел),  
    который генерирует буквы и символ до тех пока они не будут равны 
    символа из строки "hello world". То есть, в первый раз этот генератор, должен 
    закончиться тогда, когда генерируемая буква будет равна 'h' и т.д. 
    2.3 Каждый раз, когда я нахожу правильную букву, начинать генератор заново и  
    переходить на следующую букву 
    2.4 Выйти их цикла, когда мы найдем все буквы и символы 
3. Порадоваться :D

Сделать фнукцию из данных задач 
 
1. Создать программу, которое принимает 
два числа a и b (указывающие диапазон) и вычисляет количество чисел в этом диапазоне. 
Пример:    
a = 1,b = 9 -> 1,2,3,4,6,7,8,9 -> Ответ 8  
 
2. Написать программу которая проверяет, является ли число квадратом. 
Пример: скажем нам дали число 121, которе является 11^2, то есть квадратом 11. 
Если число не является квадратом другого целого (не дробного) числа, то вывести на экран -1, 
если число является правильным кваратом - вывести число возводимое в квадрат (из примера выше мы бы вернули 11)"""

# 2 
# def second_ex(a,b):
#     s = 0
#     for x in range(a,b):
#         s = s + 1
#     print(f'Деопозон между {a} и {b} = ',s)

# second_ex(1 , 9)

#3
def math_kv(num):
    if num ** 0.5 == int(num ** 0.5):
        return int(num ** 0.5)
    else:
        return -1

result = math_kv(121)
print(result)

# input_word = str(input('input the word = '))
# items = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',' ','!']

# for x in items:
#     if input_word == x:
#         print(input_word)
#     else:
#         break


# import random
# import sys
# import time
# targetArray = ["H",'e','l','l','o',',',' ','R','a','s','u','l']
# stringArray = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
# i = 0
# while i < len(targetArray):
#     if stringArray[i] != targetArray[i]:
#        stringArray[i] = chr(random.randint(32, 126))

#     if stringArray[i] == targetArray[i]:
#         i += 1

#     x = 0 
#     print("\n")
#     while x< len(stringArray):
#         print(stringArray[x], end="")
#         x += 1
#     time.sleep(.01)

# print("")