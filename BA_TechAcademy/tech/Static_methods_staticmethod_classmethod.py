"""
class StaticTest:
    x = 1

t1 = StaticTest

print(f"via instance {t1.x}")
print(f"via class {StaticTest.x}")

t1.x = 2
print(f"via instance {t1.x}")
print(f"via class {StaticTest.x}")

StaticTest.x = 3

print(f"via instance {t1.x}")
print(f"via class {StaticTest.x}")


# not Understand
"""

"""
@classmethod 
Метод класса — это метод, привязанный к классу, а не к объекту класса.
У них есть доступ к состоянию класса, поскольку он принимает параметр класса, 
который указывает на класс, а не на экземпляр объекта.
Он может изменить состояние класса, которое будет применяться ко всем экземплярам класса. 
Например, он может изменить переменную класса, которая будет применима ко всем экземплярам.
"""


"""
@staticmethod
Метод класса принимает cls в качестве первого параметра, 
в то время как статический метод не нуждается в определенных параметрах.
Метод класса может получить доступ к состоянию класса или изменить его, 
в то время как статический метод не может получить к нему доступ или изменить его.
Как правило, статические методы ничего не знают о состоянии класса. 
Это служебные методы, которые принимают некоторые параметры и работают с этими параметрами. 
С другой стороны, методы класса должны иметь класс в качестве параметра.
Мы используем декоратор @classmethod в python для создания метода класса, 
и мы используем декоратор @staticmethod для создания статического метода в python.


все инфо от - https://www.geeksforgeeks.org/class-method-vs-static-method-python/
"""


from inspect import classify_class_attrs


class Date:
    def __init__(self , month , day , year):
        self.month = month
        self.day = day
        self.year = year

    def displey(self):
        return f"{self.month} - {self.day} - {self.year}" 

    @classmethod
    def millenium_c(cls , month , day):
        return cls(month , day , 2000)

    @staticmethod
    def millenium_s(month ,day):
        return Date(month , day , 200)

d1 = Date.millenium_s(6,9)
d2 = Date.millenium_c(6,9)
        
print(d1.displey())
print(d2.displey())

class DateTime(Date):
    def displey(self):
        return f"{self.month} - {self.day} - {self.year} - 00:00PM"

dt1 = DateTime(10 , 10 , 10)
dt2 = DateTime.millenium_s(10 ,10)


class StrConverter:
    @staticmethod
    def to_str(baytes_or_str):
        if isinstance(baytes_or_str , bytes):
            value = baytes_or_str.decode('utf-8')
        else:
            value = baytes_or_str
        return value

    @staticmethod
    def to_bytes(baytes_or_str):
        if isinstance(baytes_or_str , str):
            value = baytes_or_str.encode('utf-8')
        else:
            value = baytes_or_str
        return value

call = StrConverter.to_str('\x47')
call2 = StrConverter.to_str('A')


call3 = StrConverter.to_str('\x50')
call4 = StrConverter.to_str('F')

print(call)
print(call2)
print(call3)
print(call4)


class Practic:
    def __init__(self , name , surname , age ):
        self.name = name 
        self.surname = surname
        self. age = age

    def descorp(self):
        return f"{self.surname} {self.name} {self.age}"

    @classmethod
    def code(cls , name  , surname , age):
        return cls(name , surname , age)


practic = Practic('Rasul' , 'Abduvaitov' , 20 )
s = practic.code('Rasul' , 'Abduvaitov' , 20 )
x = s.descorp()
print(x)


class Practic2:
    def __init__(self , name , surname , age):
        self.name = name 
        self.surname = surname
        self.age = age

    def descorp2(self):
        return f"{self.surname} {self.name} {self.age}"
        
    @staticmethod
    def static(surname , name , age):
        return Practic2(surname , name , age)

class_calling  = Practic2('Rasul' , 'Abduvaitov' , 20)
method=class_calling.static('Rasul' , 'Abduvaitov' , 20)
print(method.descorp2())