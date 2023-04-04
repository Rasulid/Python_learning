# name = "Javokhir"


# def find_name():
#     global name
    
#     def wsss():
#         ss = "ss"
#         return ss
#     return wsss()

# print(find_name())

# """
# Global scope
# local scope
# build in scope
# """



class Parrent:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
p_obj = Parrent(name= "Javokhir", age="13")


class Children(Parrent):
    def __init__(self, name, age):
        super(Children, self).__init__(name=name, age=age)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age


ch_obj = Children("Ras", 20)

print(ch_obj.get_name())
print(ch_obj.get_age())        



