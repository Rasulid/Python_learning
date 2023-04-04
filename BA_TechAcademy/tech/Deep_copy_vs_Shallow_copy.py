"""
Deep copy - глубокая копирования 
Shallow copy - не глубокая копирования
"""

list1 = [1,2,3,[4,5,6]]
copied_list = list1.copy()
copied_list[3].append(7)
print(list1)
print(copied_list)

print('\n')
import copy

shallow_copy = copy.copy(list1)
shallow_copy[3].append(8)
print(list1)
print(shallow_copy)

print('\n')
    
deep_copy = copy.deepcopy(list1)
deep_copy[3].append(9)
deep_copy.append(10)
print(list1)
print(deep_copy)

print('\n')


class Point():
    def __init__(self , a ,b ):
        self.a = a
        self.b = b 
    def __repr__(self):
        return f"Point {self.a} - {self.b}"

a = Point(1 ,2 )
b = copy.copy(a)
print(a)
print(b)
a.a = 5
print(a)
print(b)
    

#в не изменя емыйобекты перемен не возникает ошибки с копироаванием но 
class Line():
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
            
        return result



l1 = Line(a, b)
l2 = copy.copy(l1)

print(l1.p1)
print(l2.p1)


l1.p1.x = 4

print(l1.p1)
print(l2.p1)

l1 = Line(a, b)
l2 = copy.deepcopy(l1)

print(l1.p1)
print(l2.p1)

l1.p1.x = 6

print(l1.p1)
print(l2.p1)


