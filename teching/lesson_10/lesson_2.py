  # # def alex():
# #   print("my name is alex")


# # x = lambda a , b  :  a * b 
# # print(x(15 , 5))


# # a = {
# #   "x": 2,
# #   "y": 1
# # }

# # print(a["y"])

# # def myfunc(n):
# #   return len(n)

# # x = list(map(myfunc, ('apple', 'banana', 'cherry')))
# # print(x)

# # len()


# # Arreys  -  (Массивы)

# "Массивы используются для хранения нескольких значений в одной переменной"

# cars = ["ford","Volvo","BMW"]
# # () - tuple
# # {} - dict
# # {} - set

# # cars[1] = "mers"

# # print(cars[1])  
# # print(cars)




# # cars = {
# #   "germ":"Bmw",
# #   "engl":"astonmartin",
# #   "USA":"Ford" # mustang 
# # }

# # cars["USA"] = 'mustang'

# # print(cars["USA"])



# """
# int - целое чило 
# float - десятичное чило
# str - строка
# bool - True False
# tupl - картеж (не изменяемый)
# dict - словарь {ключ : значения}
# list - [лист , изменяемый]
# set - {изменяемый , дубликатов , у него нет определённого порядка}
# """

# """
# изменяемые 
#     list
#     dict
#     set
#     bool 



# не изменяемый 
#     int
#     str
#     tuple
#     frozen set
#     float

# """
# s = input("name = ")

# print(f"Your name is {s}") # 1
# print("Your name is {}".format(s)) # 2
# """
# if  = усдовия
# elif = усдовия
# else = итог
# """
# a = True
# if a == True:
#   print("it's True")
# elif a == None:
#   print("it's None")
# else:
#   print("it's False")


# s = list(range(11))
# print(s)

# print("\n")

# count = 0

# for x in s:
    
#     print(x)


# d = {
#   "id": 1,
#   "title": "film",
#   "desc": "some film"
# }

# for x in d.items():
#   print(x)



# def func(x):
#   for x in d.items():
#     return x

# print(func(d))



# print("heloo world")
# print("hiiiii ")


""" 
dir - показывает всё в нутри папки 
cd -  заодит в папку 
cd .. - вычодит 
Python > file-name.py - Создаёт питон файл 
py file name  - запускает питон файл 
"""




def Java(a):
    return a + 10 

# print(Java(60))

"""
      0 1 1 2 3 5 8 13 21
"""

def fibonacci(c):
    a , b = 0 ,1
    result = []
    for _  in range( c):
        x =  a + b
        a = b
        b = x 
        result.append(b)
    return result


# print(fibonacci(8))


"""
Class 
"""
class First:
    def __init__(self, name, surname, age): #__init__ magic method = ссылается в класс
        self.name = name
        self.surname = surname
        self.age = age
        
    def second(self ,a, b):
        return a + b
    

varible = First(name="First", surname="asdasd", age=12)

print(varible.second(a=12, b=12))