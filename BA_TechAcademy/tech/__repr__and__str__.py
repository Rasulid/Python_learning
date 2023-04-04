lst = [1, 2, 3]
repr(lst)
print(lst)
eval(repr(lst)) == lst
from datetime import datetime
dt = datetime.now()
repr(dt)
print(dt)

class Character():
    """this class Example"""

    def __init__(self, race, damage=100):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f"{self.race} with damage = {self.damage}"

    def __eq__(self, other):   #метод __eq__ сравнивает 2 обекта 
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False

c = Character("Elf")
print(c.__doc__)
d = eval(repr(c))
type(d)
print(d)
c == d



def name():
    """this function is working"""
    print('hello')

print(name.__doc__)


#https://www.pythontutorial.net/python-oop/python-__eq__/