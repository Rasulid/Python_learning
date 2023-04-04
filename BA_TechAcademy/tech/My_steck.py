

class MySteck:
    def __init__(self):
        self.arrey = []

    def pop(self):
        poped_item = self.arrey.pop()
        return poped_item

    def push(self , item):
        return self.arrey.append(item)

    def peek(self):
        return self.__current()

    def __current(self):
        return self.arrey[self.count()-1]

    def count(self):
        return len(self.arrey)

    def __iter__(self):
        self.index = self.count()-1

    def __next__(self):
        if self.index < 0:
            raise StopIteration()

        result = self.arrey[self.index]
        self.index -= 1
        return result


stec = MySteck(1)

print(stec.pop())