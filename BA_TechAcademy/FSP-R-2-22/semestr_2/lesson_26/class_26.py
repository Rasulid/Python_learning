MAX_TRIES = 100
def infinite(lst, iterations):
    result = ''
    iter_lst = iter(lst) # [0, 7] iteration -> next
    if lst:
        for i in range(iterations):
            try:
                result += str(next(iter_lst))
            except StopIteration:
                iter_lst = iter(lst)
                result += str(next(iter_lst))
            
    return result

print(infinite([0, 7], 7))

print(__name__)


if __name__ == '__main':
    # print('run this')
    print(__name__)