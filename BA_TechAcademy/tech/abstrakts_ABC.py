from abc import ABC
from abc import abstractmethod


class Shape(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def drang(self):
        pass
        
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        print('Calc  perimetr')
        # pass

    
# s = Shape()
# print(s.perimetr)
    
import math
class Triangle(Shape):

    def __init__(self  , a,b,c) -> None:
        super().__init__()
        self.a= a
        self.b=b
        self.c = c

    def draw(self):
        return f'Drawing triangle method {self.a} , {self.b} , {self.c}'

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a ) * (s - self.b) * (s - self.c))

    def perimetr(self):
        print(self.a + self.b + self.c)
    
    def drang(self):
        super().drang()
        print('Aditional actions')


t = Triangle(10,10,10)
t.perimetr()

"""
@abc.abstractmethod
Декоратор, указывающий абстрактные методы.

Использование этого декоратора требует, чтобы метакласс класса был ABCMeta производным от него. 
Класс, производный от метакласса, ABCMetaне может быть создан, пока не будут переопределены все его абстрактные методы и свойства. 
Абстрактные методы могут быть вызваны с использованием любого из обычных «супер» механизмов вызова. 
abstractmethod()может использоваться для объявления абстрактных методов для свойств и дескрипторов.

Динамическое добавление абстрактных методов в класс или попытка изменить статус абстракции метода или 
класса после его создания поддерживаются только с использованием update_abstractmethods()функции. 
Это abstractmethod()влияет только на подклассы, полученные с использованием обычного наследования; 
«виртуальные подклассы», зарегистрированные с помощью метода ABC, register() не затрагиваются.
"""


