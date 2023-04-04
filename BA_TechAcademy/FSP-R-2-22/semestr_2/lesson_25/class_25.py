# try:
#     a = 1/0

# except Exception as err:
#     print(err)

# print('working')

# class A:
#     pass

# print(Exception.mro())

# class WrongInputError(Exception):
#     """Происхождение """


# inet[0] <-- не работает

# не обязательно писaть iter(...) для range, generator, map, filter, files. Потому что они сами Итераторы 
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

itr = iter(l)
print(itr)
val = next(itr)
print(val)

def a():
    print(next(itr))
a()

print(next(itr))
print(next(itr))
print(next(itr))



gen = (x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
print("works")

l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

l = [1, 2, 3, 4, 5]
for i in l:
    print(i) 


def make_list(num):
    result = []
    for i in range(num):
        result.append( i + 2 )
    return result

# my_list = make_list(1000)
# print(my_list)

def generator_func(num):
    for i in range(num):
        yield i + 2
        print('addfsa')
    
g = generator_func(5)
# print( next(g) )
# print( next(g) )
# print( next(g) )
# print( next(g) )
# print( next(g) )
# print( next(g) )
for i in generator_func(100):
    print(i)

