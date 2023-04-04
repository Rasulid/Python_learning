class Charecter2:
    def __init__(self) -> None:
        self.c = 'Charecter - 2'

c = Charecter2()
print(c.c)
# print(c.rais)

c.c = "r"
print(c.c)
print(c.c)


class Charecter():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance= super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.rais = 'rais'

        
c = Charecter()
print(c.rais)
# print(c.rais)

c.rais = "r"
print(c.rais)
print(c.rais)

# https://www.geeksforgeeks.org/__new__-in-python/

class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
    
print(A())

class A(object):
    # new method returning a string
    def __new__(cls):
        print("Creating instance")
        return "GeeksforGeeks"
  
class B(object):
    # init method returning a string
    def __init__(self):
        print("Initializing instance")
        # return "GeeksforGeeks"
  
print(A())
print(B())
"""
Этот TypeError вызывается обработчиком, который вызывает метод __init__, 
и даже не имеет смысла возвращать что-либо из метода __init__, 
поскольку его цель — просто изменить свежее состояние вновь созданного экземпляра.
"""