#map__________________________________________________________________
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


#filter__________________________________________________________________
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

#Decorator__________________________________________________________________

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

print('\n')

#decorator @wraps__________________________________________________________________

def log_decoretion(func):
    def wrap():
        print(f"Calling functon {func}")
        func()
        print(f"Function is worked {func}")
    return wrap

@log_decoretion
def hello():
    print("Hello world")

print(hello())
print(help(hello))

from functools import wraps

def log_decoretion(func):
    @wraps(func)
    def wrap(*args , **kwargs):
        print(f"Calling functon {func}")
        func(*args ,*kwargs)
        print(f"Function is worked {func}")
    return wrap

@log_decoretion
def hello():
    print("Hello world")

print(hello())
print(help(hello))

from this import d

#whos is first__________________________________________________________________

def whos_first(p1, p2):
    # ваше решение
    diss = p1.find('B') -  p2.find('B')
    if diss < 0:
        return 'p1'
    elif diss > 0:
        return 'p2'
    else:
        return 'tie'

print(whos_first("   Bang!        ",
                 "        Bang!   "))

# summ__________________________________________________________________
  
def solve_hanoi_tower(discks):
    return 2**discks - 1

print(solve_hanoi_tower(5))


def summa(lst):
    return sum([ a+b for a,b in lst]) if not any([a==b for a,b in lst]) else 0

print(summa([(1, 2), (3, 4), (5, 6)]))

#any dublicates__________________________________________________________________


def any_duplicates(squere):
    sor = [ i for x in squere for i in x]
    return sorted(sor) != [1,2,3,4,5,6,7,8,9]

print(any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]]))


#sticks game__________________________________________________________________


number_of_sticks = 10
player_turn = 1

while number_of_sticks > 0:
    print(f'How many sticks you teken? Remennig {number_of_sticks}')
    take = int(input())

    if take < 1 or take > 3:
        print(f'You tride to teke {take} . Allowed to take 1,2,3 sticks')
        continue
    number_of_sticks -= take
    print(f'Sticks taken {take}\n')

    if number_of_sticks <= 0:
        print(f'No more stick in the game.\n Player {player_turn} has lost')

    player_turn = 1 if player_turn == 2  else 2



number_of_sticks = 10
player_turn = 1

def can_take(sticks):
    return sticks >= 1 and sticks <= 3

def switch_player_turn(turn):
    return 1 if turn == 2 else 2

def end_of_game(sticks):
    return sticks <= 0

while (not end_of_game(number_of_sticks)):
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())
    
    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks.')
        continue
    
    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')
    
    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost!')
        break
    
    player_turn = switch_player_turn(player_turn)

