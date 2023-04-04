import random


def rondom_int(num_1 , num2):
    try:
        return random.randint(num_1,num2)
    except Exception as err:
        print(err)

print(rondom_int(0 , 10))