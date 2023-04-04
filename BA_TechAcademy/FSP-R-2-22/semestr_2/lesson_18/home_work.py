from datetime import date


class My_info:
    my_born_day = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info_on_desctop(self):
        return f"{self.name} {self.surname} {self.get_age()}"

    def get_age(self):
        My_info.my_born_day = (date.today().year - self.age)


info = My_info("Rasul", "Abduvaitov", 19)
print(info.get_info_on_desctop())
print(info.get_age())
