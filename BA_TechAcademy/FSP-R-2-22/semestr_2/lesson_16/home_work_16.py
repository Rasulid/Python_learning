"""
Задача 4. 
Напишите программу с классом Car. 
Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
Третий — присвоение автомобилю года выпуска. 
Четвертый метод — присвоение автомобилю типа. 
Пятый — присвоение автомобилю цвета.

"""
from tokenize import group


class Car:
    def Car (self , colour , cartype , year):
        self.colour = "Чёрный"
        self.type = "Лёгкий седан"
        self.year = 2022

    def zapusk (self):
        return 'Автомобиль заведён'
    
    def zaglushka(self):
        return 'Автомобиль заглушон'

    def avto_year(self):
        return self.year

    def avto_type(self):
        return self.cartype 

    def avto_colour(self):
        return self.colour

calling = Car()
calling_func = calling.zapusk()
calling_func = calling.zaglushka()
calling_func = calling.avto_year()
calling_func = calling.avto_type()
calling_func = calling.avto_colour()


"""
Задача 1. 
Необходимо реализовать код, показанный в примерах выше. 
Создать класс Rectangle и класс ToyClass. 
Для ToyClass необходимо добавить три атрибута, и метод который устанавливает их.

Задача 2. 
Напишите программу с классом Student, 
в котором есть три атрибута: name, groupNumber и age. 
По умолчанию name = Ivan, age = 18, groupNumber = 10A. 
Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. 
Метод getName нужен для получения данных об имени конкретного студента, 
метод getAge нужен для получения данных о возрасте конкретного студента, 
метод setGroupNumber нужен для получения данных о номере группы конкретного студента. 
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
В программе необходимо создать пять экземпляров класса Student, установить им разные имена, 
возраст и номер группы.

Задача 3. 
Напишите программу с классом Math. 
Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. 
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

"""


class Ractangle:
    pass

class ToyClass:
    def __init__(self , disgn , what , colour):
        self.disgn = disgn
        self.what = what
        self.colour = colour

toy_class = ToyClass('standart' , 'boll', 'black')


# Напишите программу с классом Student, 
# в котором есть три атрибута: name, groupNumber и age. 
# По умолчанию name = Ivan, age = 18, groupNumber = 10A. 
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. 
# Метод getName нужен для получения данных об имени конкретного студента, 
# метод getAge нужен для получения данных о возрасте конкретного студента, 
# метод setGroupNumber нужен для получения данных о номере группы конкретного студента. 
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, 
# возраст и номер группы.

class Student :
    name = "Ivan"
    age = 18
    groupNumber = '10A'
    univer = 'TIUE'
    lave = 'Tashkent'

    def getname(self):
        input('get name the student =',self.name)
    def getAge(self):
        input('get age the student = ' , self.age)
    def setGroupNumber(self):
        input('set number the student = ' , self.groupNumber )
    def setTheUniver(self):
        input('set the University = ' , self.univer)
    def live(self):
        input('where he live = ' ,self.lave )


# Напишите программу с классом Math. 
# Создайте два атрибута — a и b. 
# Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. 
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.


class Math:
    a = 10
    b = 10
    def addition(self ):
        x = self.a + self.b
        return x 

    def multiplication(self ):
        x = self.a * self.b
        return x 

    def division(self ):
        x = self.a / self.b
        return x 

    def subtraction(self ):
        x = self.a - self.b
        return x 