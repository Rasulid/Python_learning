# # исключения
# try :
#     a = 12
#     a / 0
# except ZeroDivisionError:
#     print("ZeroDivisionError")


# try:
#     import ark
# except ImportError:
#     print("ImportError")



# try:
#     import ark
# except Exception as er:
#     print(er)


# print('jervnjernqjr')
# print(Exception.mro())


# while True:
#     try:
#         a = int(input('Enter your age = '))
#         print(a)
#     except:
#         print('Enter the number ')

#     else:
#         print('thenk you!!')
#         break

#     finally:
#         print('работает всегда')


# if 1 == 1 :
#     raise AssertionError('some error massage')

# else:
#     print('yes')


class NetworkError(Exception):
    pass

if "nat" != "server":
    raise NetworkError