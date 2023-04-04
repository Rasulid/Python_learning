import re


class Vehile:
    def __init__(self , position):
        self.position = position


    def calculate_rout(self , sourse , to ):
        return 0

    def trevel(self,destination):
        rout = self.calculate_rout(sourse = self.position , to = destination)
        self.move_along(rout)

    def move_along (self , route):
        print('move it ')

class Car(Vehile):
    pass

class Airplane(Vehile):
    pass

class RadioMixin:
    def __init__(self) -> None:
        self.radio = Radio()
    
    def turn_on(self,station):
        self.radio.set_station(station)
        self.radio.play()

class Radio:
    def set_station(self , station):
        self.station = station

    def play(self):
        print(f'Plaing {self.station}')

class Car(Vehile , RadioMixin):
    def __init__(self):
        Vehile.__init__(self , (10 , 20))
        RadioMixin.__init__(self)
        
car = Car()

# print(car.turn_on('Toshkent sadossiiii'))


class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
            
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value
        
class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# In[ ]:


tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())



# In[ ]:


tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())