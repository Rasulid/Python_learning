def zipWith(func , a1 = [10,10,10,10] , a2= [0,1,2,3,4,5]):
    new_result = []
    result = list(zip(a1,a2))
    for val in result:
        new_result.append(func(val))

    return new_result
print(zipWith(max))

a = lambda x, y : x+y
print(a(10,30))

class A:
    def get_name(self):
        print("a")

class B:
    def get_name(self):
        print('b')

class C (A):
    pass

class D (C , B):
    pass

d = D
d.get_name()
print(d.mro())