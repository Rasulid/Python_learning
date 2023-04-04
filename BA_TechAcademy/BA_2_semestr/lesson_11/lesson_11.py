# import calendar
# yy = 2022
# mm = 10
# print(calendar.month(yy , mm))

def siq(numbers):
    return numbers * numbers

numbers = [1,2,3,4,4,5,6,6]

for x in map(siq , numbers):
    print(x)


def coordinate(coord,value):
    result = zip(coord , value)
    result_list = list(result)
    print(result_list)

    c , v = zip(*result_list)
    print('c =',c)
    print('v =', v)

print('\n')

coo=coordinate(['x','y','z'] , [1,2,3])
print(coo)

print('\n')


#filter
def is_adult(age):
    return age>=18

age = [14,18,16,21,15,30]

filtered_list = list(filter(is_adult,age))
print(filtered_list)

for x in filter(is_adult,age):
    print(x)

print('\n')

is_adult = lambda age : age>=18
age = [14,18,16,21,15,30]

for x in filter(is_adult , age):

    print(x)



print(list(filter(lambda age:age>=18 , age)) )

print('\n')

multiplayr = lambda x,y: x*y

print(multiplayr(5,3))

print('\n')

my_list =[1,2,3,4,5,6,7,8,9,10,11,12]
new_list = list(map(lambda x:x*2 , my_list))
print(new_list)
print('x = ',x)

print('\n')

def log_decorator(func):
    def wrap():
        print(f'calling func {func}')
        func()
        print(f'func {func} is finished ')
    return wrap()

def hello():
    print('hello world')

wraped_by_logg = log_decorator(hello)
print(wraped_by_logg)

print('\n')

@log_decorator
def hello():
    print('hello world')
he=hello
print(he)

print('\n')

from timeit import default_timer as timer
import math
import time

def first_f(func):
    def second_f(*args,**kwargs):
        start = timer()
        func(*args,**kwargs)
        end = timer()

        print(f'Function {func.__name__} took {end-start} for ')
    return second_f

@first_f
def factor(num):
    time.sleep(3)
    print(math.factorial(num))

print(factor(100))



