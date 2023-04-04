"""1. Используйте функцию по нахождению ряда фиббоначи, 
написать декоратор, который будет вычислять время его работы.

2. Используя функцию по нахождения факториала, написать декортор, 
который будет запускать его два раза и вычислять общее время запуска."""




import timeit
def time():
    elapsed_time = timeit.timeit()
    return elapsed_time


def fibonachi():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")

    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1 , sep='\n')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    def fibonachi_2(func):
        print('2 раз')
        func()
    return fibonachi_2(fibonachi)
    

f = fibonachi()
print(f) 