import sys 
import random

a = int(sys.argv[1])
b = int(sys.argv[2])
lifes = 3

x = random.randint(a , b)
print(sys.argv)

def find_number(x):
    return num == x

print(f"вам нужно найти числа в диапазоне {a}-{b}")

while True:
    num = int(input('Велите число ='))
    result = find_number(x)

    if result:
        print('вы выграли!!')
        break

    elif lifes == 1:
        print("Жизнь закончилось!")
        break

    else:
        lifes -= 1
        print("Попробуйте ещёраз!")
    