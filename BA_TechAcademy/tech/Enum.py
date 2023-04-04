from enum import Enum

# class TrafficLigts(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3

# print(TrafficLigts(1))
# print(TrafficLigts.RED)
# print(TrafficLigts.RED.name)
# print(TrafficLigts.RED.value)
# print(TrafficLigts.RED == TrafficLigts.RED)
# print(TrafficLigts.RED == TrafficLigts.GREEN)

# from enum import IntEnum
# class Priority(IntEnum):
#     LOW = 1
#     POW = 2
#     SEW = 3
#                 #менше
# print(Priority.LOW < Priority.SEW)


from enum import IntFlag

# class Colour(IntFlag):
#     RED = 1
#     BLUE = 2
#     GREY = 3

# combination = Colour.RED | Colour.BLUE

# print(Colour.BLUE in combination)
# print(Colour.GREY in combination)
# print('https://docs.python.org/3/library/enum.html',
# 'https://www.programiz.com/python-programming/examples/represent-enum')



# class Planet(Enum):
#     MERCURY = (3.303e+23, 2.4397e6)
#     VENUS   = (4.869e+24, 6.0518e6)
#     EARTH   = (5.976e+24, 6.37814e6)

#     def __init__(self , radius , mass):
#         self.mass = mass
#         self.radius = radius

#     @property
#     def surface_gravity(self):
#         G = 6.67300E-11
#         return G * self.mass/(self.radius * self.radius)
        
# print('https://www.programiz.com/python-programming/property')
# print(Planet.EARTH.value)
# print(Planet.EARTH.surface_gravity)




class EnumPracis(IntFlag):
    RASUL = 19
    MIRAZIZ = 22
    OGABEK = 19

print(EnumPracis.RASUL == EnumPracis.MIRAZIZ)
print(EnumPracis.RASUL == EnumPracis.OGABEK)

cop = EnumPracis.RASUL | EnumPracis.MIRAZIZ | EnumPracis.OGABEK

print(EnumPracis.OGABEK in cop)

