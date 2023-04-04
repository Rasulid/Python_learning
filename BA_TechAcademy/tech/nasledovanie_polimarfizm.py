from shelve import Shelf


class Shape :
    def __init__(self):
        print('Shape is work')
    def draw(self):
        # raise NotImplementedError ("Can't instantiant an abstract class")
        print('Shape is draw')

    def area(self):
        # raise NotImplementedError ("Can't instantiant an abstract class")
        print('Shape is area')

    def perimetr(self):
        # raise NotImplementedError ("Can't instantiant an abstract class")
        print('Shape is perimetr')

# shape = Shape()
# print(shape)


class Rectangle(Shape):
    def __init__(self , high , width):
        Shape.__init__(self)
        self.high = high
        self.width = width

        print('Rectengle create')

        Shape.area(self)
    def area(self):
        return self.width * self.high
    
    def perimetr(self):
        return 2 * (self.high + self.width)

    def draw(self):
        print(f"Drawing rectangle with width = {self.width}  and high = {self.high}")

rect = Rectangle(10 , 15)
print(rect.draw() , rect.perimetr() , rect.area() , sep="\n")

import math
class Triangle (Shape):

    def __init__(self , a , b , c):
        super().__init__()

        self.a = a
        self.b = b 
        self.c = c 

        print('Triangle Created')

    def draw(self):
        print(f'Drawing triangle whith sides ={self.a} , {self.b} , {self.c}')
        

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))

    def perimetr(self):
        return self.a + self.b + self.c

triangle = Triangle(10 ,10 ,10)
print(triangle.perimetr())

# Если 2 класса имеют одинаковые методи и названия - мы используем 
"""полимарфизм"""
for shape in [rect , triangle]:
    shape.draw()


            

    