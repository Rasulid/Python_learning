import datetime


class Pleyer:
    def __init__(self, x):
        self.x = x 

    @classmethod
    def overal_init(self , cls , x):
        return cls(x * 2)

    # def __str__(self) -> str:
        # return f' x = {self.x}'

    def __repr__(self) -> str:
        return f'in repr x = {self.x}'

    
pleyer = Pleyer(12)
print(pleyer)

date = datetime.datetime(2003 , 11 , 30 , 14 , 24)
print(str(date) , repr(date) , sep='\n')

"""
a + b       a.__add__(b) 
a - b       a.__sub__(b) 
a * b       a.__mul__(b) 
a / b       a.__truediv__(b) 
a // b      a.__floordiv__(b) 
a % b       a.__mod__(b) 
a << b      a.__lshift__(b) 
a >> b      a.__rshift__(b) 
a & b       a.__and__(b) 
a | b       a.__or__(b) 
a ^ b       a.__xor__(b) 
a ** b      a.__pow__(b) 
-a          a.__neg__() 
~a          a.__invert__() 
abs(a)      a.__abs__()
"""

