"""
Основы ООП (Объектно Ориентиованное Программирование): 
    Наследование -  
    Полиморфизм - это единный интерфейс для операций над разными типами данных 
        + 
        2 + 2 = 4 
        '2' + '2' = '22' 
        [2, 3] + [4, 5] = [2, 3, 4, 5] 
        len("fdf") 
    Инкапсуляция -  
    Абстракция (просто знать название) 
 
переменные класса - это аргументы 
функции класса - это методы 
 
Функциональное программирование 
"""

class Person:
    __super_sicret = 'secret '
    pi = 3.14
    def __init__(self , name , surname):
        self.name = name
        self.surname = surname
        self.age = 19

    def get_full_name(self):
        return f'My name is {self.name} and my surname is {self.surname}'

        



person_1 = Person('Rasul' , 'Abduvaitov')
print(person_1.name , person_1.surname , person_1.age , person_1.pi)
full_name = person_1.get_full_name()
print(full_name)
        


person_2 = Person('Bitch' , 'Ass')
print(person_2.name , person_2.surname , person_2.age)
full_name_2 = person_2.get_full_name()
print(full_name_2)


print(dir(Person))


print(Person.__super_sicret)
