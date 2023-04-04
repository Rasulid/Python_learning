class Person :
    _secret = 'birth day'
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
    def get_info(self):
        return f'name {self.name} age {self.age}'

    def get_age(self):
        return self.age

person = Person('gibby' , 21)
        
