def function (func):
    func()
    return 2

def geeting():
    print("AUE")

name = "Name"

def wrapper():
    def hello_world():
        return 'Hello world'
    return hello_world()

print(wrapper())


def my_deg(func):
    def wrapper():
        print('something')
        func()
        print('hi')
    return wrapper()

@my_deg
def hello():
    print('def hello')

# print(my_deg(hello))
print(hello)
    