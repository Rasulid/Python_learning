import json

class Turnamed:
    def __init__(self , name , year):
        self.name = name
        self.year = year

tournaments = {
     "Aeroflot Open": 2010,
     "FIDE World Cup": 2018,
    "FIDE Grand Prix": 2016
 }
json_data = json.dump(tournaments, indent=2) # serializing
print(json_data)

 # some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

 # parse x:
y = json.loads(x)

 # the result is a Python dictionary:
print(y["age"])

# from json import dumps

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# #  в этом библеотеке возникается ошибка 
# #https://github.com/EngineerSpock/Python-from-Zero-to-Hero/blob/master/08-%D0%94%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE/09-json%20fundamentals.py


