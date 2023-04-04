def simpleGenerator():
    yield 1
    yield 2
    yield 3

for x in simpleGenerator():
    print(x)