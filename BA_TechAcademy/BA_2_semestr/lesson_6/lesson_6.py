# from unicodedata import name
# name = "john"
# print(name)

# def spaan ():
#     global name
#     name = 'santa'
# spaan()
# print(name)

# def foo (items):
#     items.append(42)

# a = [0,1,2,3,4,5,6]
# foo(a)
# print(a)

# def bar(items):
#     items = [4,5,6]

# b = [1,2,3]
# bar(b)
# print('b не изменилось ' , b)

# a = [2,3,4,5]
# a.append(45)
# a = [6,78,89,]


from this import s


def star(number):
    for s in range(number):
        print('*' * (s + 1))

star(3)





"""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

"""
def like_or_dislike(lst):
    state = 'Nothing'
    for i in lst:                                    # изучить код 
        state = 'Nothing' if i == state else i
    return state
"""

"""def feast(beast, dish):
    return beast[0]==dish[0] and dish[-1]==beast[-1]
    """


def summation(num):
    i = 0
    for s in range(num + 1):
        i = i + s
    return i