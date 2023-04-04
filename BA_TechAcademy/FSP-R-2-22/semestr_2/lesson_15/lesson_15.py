from zoneinfo import available_timezones


class Pleyer:
    available_spesializations = {'Силу':"Сила" , "Разум":"Разум","Ловкость":"Ловкость"}
    available_abilities = {
        "сила" : ("Таран"),
        "разум" : ("Огниный шар"),
        "ловкость" : ("Уклонения")
    }
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.health = 100
        self.abilities = []
        self.spesialization = ""
        self.items = []

    def begining():
        pass

    def login(self , username , password):
        if self.username == username and self.password == password :
            print('you loged sicsesfuly ')
        else :
            print("User name or password invaild ") 

    def choose_spesialization(self , spesialization):
        if spesialization in self.available_spesializations.values() :
            self.spesialization = spesialization
            self.create_hero()
            
        else:
            print("Вы выбрали не правельную спецыализацыю")
  
    def create_hero(self):
        if self.spesialization == self.available_spesializations["Силу"]:
            self.health = 200
            self.abilities == self.available_abilities[self.spesialization.lower()]
            self.items = "молот"
            print(f"Вы выбрали {spesialization} \nУ вас есть {self.items} \nВаше здоровье {self.health}")

        if self.spesialization == self.available_spesializations["Разум"]:
            self.health = 150
            self.abilities == self.available_abilities[self.spesialization.lower()]
            self.items = "посох"
            print(f"Вы выбрали {spesialization} \nУ вас есть {self.items} \nВаше здоровье {self.health}")

        if self.spesialization == self.available_spesializations["Ловкость"]:
            self.health = 300
            self.abilities == self.available_abilities[self.spesialization.lower()]
            self.items = "Мечь"
            print(f"Вы выбрали {spesialization} \nУ вас есть {self.items} \nВаше здоровье {self.health}")

strenght = Pleyer('Alloha' , '123rasul')
username = 'Alloha'
password = '123rasul'    
strenght.login(username , password)
spesialization = str(input('выбирите способность (Сила , Разум , Ловкость) = '))
strenght.choose_spesialization(spesialization)

