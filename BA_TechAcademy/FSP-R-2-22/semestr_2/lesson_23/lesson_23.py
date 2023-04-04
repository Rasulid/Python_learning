from time import time



def do_twise(func):
    def wrapped(n):
        start = time()
        print('result 1 ="' , func(n))
        print('result 2 ="' , func(n))
        end = time()

        return f'time working {end - start}'
    return wrapped 

def factorial(n):
    if n < 0:
        return 1

    fact = 1
    for i in range(1 , n+1):
        fact *= i
    return fact

result = do_twise(factorial)(10)
print(result)


def m2(func):
    def m1(s , c):
        return func(s , c) * 2
    return m1

@m2
def multiplay(x , y):
    return x * y

print(multiplay(10 , 2))


def get_sum(s , * , g): # обезательный ключевой оргумент 
    print(g)
    return sum(s)

print(get_sum([1,2,3,4] , g=100))



