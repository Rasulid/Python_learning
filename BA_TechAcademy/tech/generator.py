#lasy evaluation 
import random

def gen(min , max , n):
    return [random.randint(min , max) for _ in range(n)]   #он сохраняет в памяте

for i in gen(20 , 30 , 5):
    print(i)

print('\n')

def lasy_avaluation(min , max , n):
    for i in range(n):
        yield random.randint(20 , 30)   #а он нет оно нам позволяет не загружать память



for i in lasy_avaluation(20 , 30 , 5):
    print(i)

type_the_lasy_evaluation = lasy_avaluation(10 , 40 , 3)
print(type_the_lasy_evaluation)