from copy import deepcopy
from os import name


class Stock:
    def __init__(self , name , shares , price):
        self.name = name 
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell (self , nshares):
         self.shares -= nshares 

class Stock_2:
    n = 100
    def __init__(self,random):
        self.random = random
    def go(self):
        print(self.random)


class Mystock(Stock , Stock_2):
    def __init__(self, name, shares, price ,random, funds):
        super().__init__(name, shares, price)
        self.funds = funds
        self.random = 12

    def cost(self):
        return self.funds * super().cost()

    
my_stock = Mystock('Golden house' , 50 , 50000 ,12, 10000)
print(my_stock.cost())
my_stock.sell(10)
my_stock.go()
print(my_stock.shares , my_stock.n , my_stock.random)       