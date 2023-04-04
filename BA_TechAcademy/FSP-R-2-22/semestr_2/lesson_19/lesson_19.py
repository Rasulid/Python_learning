# class Animal:
#     def __init__(self, name, species, age, health, weight, color):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.health = health
#         self.weight = weight
#         self.color = color




# def make_class(*args):
#     colling_class = Animal(*args)
#     return colling_class



# dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
# dog2 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")

# print(make_class("Bob", "Dog", 5, "good", "50lb", "brown")) 


# def shades_of_grey(n, start=1):
  

#   if (n < 1) or (start < 0):
#       return []
#   elif n > 254:
#       n = 254
  
#   end = start + n
#   if end > 255:      
#     end = 255
  
#   return [
#       '#{h:0>2x}{h:0>2x}{h:0>2x}'.format(h=i)
#       for i in range(start, end)
#   ]

# print(shades_of_grey(1))
# print(shades_of_grey(2))
# print(shades_of_grey(3))
# print(shades_of_grey(4))
# print(shades_of_grey(5))
# print(shades_of_grey(6))
# print(shades_of_grey(7))
# print(shades_of_grey(8))
# print(shades_of_grey(9))
# print(shades_of_grey(10))

# #не очень понял 
    

def check_even(x):
    return True if x % 2 == 0 else False #ternal even 

print(list(filter(check_even , [1,2,3,4,5,9,6,7,8,])))



def finc(*args , **kwargs):
    return args , kwargs


func = finc(1,2,3,4 , [234,531] , {1:'dsf'} , sde = 'dsvtwb', rasge = '100')
print(func)


f = list(filter(lambda x : x * 2 if x % 2 == 0 else 0 , [2,3,4]))
m = list(map(lambda x : x * 2 if x % 2 == 0 else 0 , [2,3,4]))


print(f,m)


class ListClass(list):
    pass

l = ListClass()
l.append(103254)
print(l)