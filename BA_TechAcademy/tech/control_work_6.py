class Employee:
    def __init__(self , first_name , last_name ,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    
    @classmethod
    def from_string(cls , pere_op):
        first_name , last_name,salary = pere_op.split('-')
        return cls(first_name , last_name, int(salary))




class Name:
    def __init__(self ,first_name ,last_name):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = self.first_name + ' ' + self.last_name
        self.initials = self.first_name[0] + "." + self.last_name[0]



class Pizza:
    order = 0
    
    def __init__(self,ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order
        
    @classmethod   
    def hawaiian( cls):
        return cls(['ham','pineapple'])
        
    @classmethod 
    def meat_festival( cls):
        return cls(['beef', 'meatball', 'bacon'])
        
        
    @classmethod
    def garden_feast (cls):
        return cls(['spinach', 'olives', 'mushroom'])







from dataclasses import replace
import math

class Circle:
    
    def __init__(self , r = 0):
        self.r = r
        
    def get_area(self):
        return math.pi * self.r ** 2
        
    def get_perimeter(self):
        return 2 * math.pi * self.r


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']







def print_state(state):
    for i, c in enumerate(state):
        if (i+1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')



print_state(board)


winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''




def play_game(board):
    current_sign = 'X'
    while(get_winner(board, winning_combinations)==''):
        index = int(input(f'Where you want to draw {current_sign}?'))
        board[index] = current_sign
        
        print_state(board)
        
        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f'We have a winner:{winner_sign}')        
        
        current_sign = 'X' if current_sign == 'O' else 'O' 




play_game(board)
play_game(board)