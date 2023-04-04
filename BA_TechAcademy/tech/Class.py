from email import header


"""class Charecter:

    def __init__(self , rase , damege = 40  , armour = 59 )  :
        self.rase = rase
        self.damege = damege
        self.armour = armour 

unit = Charecter("ahad")
print(type(unit))
print(unit.rase)
print(unit.damege)
print(unit.armour)"""

#Атрибуты и Методы 
"""
self -  Это не ключевое слова , а просто соглашения об именовании 
"""
class Game:
    max_speed = 100
    dead_health = 0 
    def __init__(self , rase , demege=10 , armour=20):
        self.rase = rase 
        self.demege = demege 
        self.armour = armour 
        self.health = 100

    def hit(self , demege):
        s = self.health
        x = demege
        return s - x

    def is_dead(self):
        return self.health == Game.dead_health

game = Game('Welcome')
print(game.hit(80))
print(game.is_dead())