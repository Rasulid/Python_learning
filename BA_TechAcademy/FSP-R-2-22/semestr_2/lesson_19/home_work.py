
get_sum = lambda n:((n + 1 )*(n + 2 )*(4 * n+3)) // 6 



print(get_sum(0))  #1
print(get_sum(1))  #7
print(get_sum(2)) #22
print(get_sum(3)) #50


# 1. https://www.codewars.com/kata/6357825a00fba284e0189798/train/python



def count_loop_iterations(arr):
    res = []
    acc = 1
    for n, b in arr:
        n = n + 2 if b else n + 1
        res.append(acc * n)
        acc *= n - 1
    return res

print(count_loop_iterations([(4, True), (5, False), (3, True)]), [6, 30, 125])
print(count_loop_iterations([(16, False), (11, False), (1, True), (3, False), (8, True), (10, True), (9, False), (11, True), (20, True), (3, False), (7, False)]), [17, 192, 528, 1408, 10560, 114048, 1045440, 12231648, 248396544, 948423168, 5690539008])
print(count_loop_iterations([]), [])
print(count_loop_iterations([(20, False)]), [21])


#3.https://www.codewars.com/kata/633bbba75882f6004f9dae4c/train/python