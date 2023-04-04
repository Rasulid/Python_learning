# https://habr.com/ru/post/44599/
try:
    import cPickle as pickle
    obj = {"one": 123, "two": [1, 2, 3]}
except ImportError:
    print('чтото не так с библиотекой (')