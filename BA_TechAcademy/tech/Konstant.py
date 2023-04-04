# Константы. Защещённые и приватные атрибуты.Свойства
class Charecter:
    MAX_VALUE = 100 # согласно по логику прогр. нельзя трогать verbls с большим регистром
    def __init__(self , rase , damege = 40  , armour = 59 )  :
        self.__rase = rase
        self.damege = damege
        self.armour = armour 
        self._health = 100
        self._current_speed = 80

    def bit(self , damege):
        self._health -= damege

    @property
    def race(self):
        return self.__rase

    @property
    def health(self):
        return self._health

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self , current_speed):
        if self.current_speed > 0:
            current_speed = 0
        elif self.current_speed > 100:
            current_speed = 100
        else:
            self.current_speed =current_speed
s = Charecter(90)
print(s._Charecter__rase) #вот так вызывать приватное переменное в Python
print(s._health)

"""
Если мы хотм использовать приватную переменную в методе или наследование ,
то пишем с одной нижней чертой "_", но если мы не хотим его использовать ,
то пишем с двумя нижними чертами "__".
"""

# print(s.health())