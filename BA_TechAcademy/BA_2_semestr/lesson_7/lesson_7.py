# import numbers


# def chuck_push_ups(chuck):
#     max_bin_num = 0 
#     if isinstance(chuck , str):
#         if '0' in chuck and '1' in chuck:
#             for word in chuck.split():
#                 binary_str = ''
#                 for val in word:
#                     if val == '1':
#                         binary_str += val
#                     elif val == '0':
#                         binary_str += val

#                 if binary_str != '':
#                     max_val = int(binary_str , 2) 
#                     if max_bin_num < max_val:
#                         max_bin_num = max_val
                    
#             return max_bin_num
        
#         else :
#             return 'CHUCK SMACH !!!'

#     else:
#         return 'FAILL !!!'

# print(chuck_push_ups(' 1 Chuck 10 stop that ! 11 Your vest looks stupid  100 101 110'))




# number= [1,2,3]
# print(help(number.append(6)))


# from statistics import mean


# inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88] 
# list_avg = mean(inp_lst)
# print(list_avg)

# sum_lst = sum(inp_lst) 
# lst_avg = sum_lst/len(inp_lst)

# import random

# def find_average(numbers):
    
#     sum_list = sum(numbers)
#     list_avg = sum_list/len(numbers)
    
#     return list_avg
    

# def star_2(n):
#     i = 1
#     m = '*'
#     s = n // 2
#     prob = ' '
#     while i <= n:
#         res = s * prob
#         tot = res + ( i * m )
#         s -= 1
#         i += 2
#         print(tot)
#     s = n // 2
#     print(((s*prob)+(m*1)),((s*prob)+(m*1)),sep='\n')
    
# star_2(5)


 
# Name      Share      Price     Change 
# ---------- ---------- ---------- ---------- 
#         AA        100      39.91       7.71  
#        IBM         50     106.11      15.01  
#         AA        100      39.91       7.71  
#        IBM         50     106.11      15.01

def Sheets(a,b,c,d):

    if a:
        keys_a = a.keys()
        for_function = [x for x in keys_a]
        len_keys = len(for_function)
        if len_keys >= 4:
            f = "{0:>10} {1:>10} {2:>10} {3:>10}".format(for_function[0],for_function[1],for_function[2],for_function[3])
        elif len_keys == 3:
            f = "{0:>10} {1:>10} {2:>10}".format(for_function[0],for_function[1],for_function[2])
        elif len_keys == 2:
            f = "{0:>10} {1:>10}".format(for_function[0],for_function[1])
        elif len_keys == 1:
            f = "{0:>10}".format(for_function[0])




        if len_keys > 4:
            tab = (('_')*10+' ') * 4
        else:
            tab = (('_')*10+' ') * len_keys

        values = a.values()
        for_function_2 = [x for x in values]
        if len_keys >= 4:
            f_2 ="{0:>10} {1:>10} {2:>10} {3:>10}".format(for_function_2[0],for_function_2[1],for_function_2[2],for_function_2[3])
        elif len_keys == 3:
            f_2 ="{0:>10} {1:>10} {2:>10}".format(for_function_2[0],for_function_2[1],for_function_2[2])
        elif len_keys == 2:
            f_2 ="{0:>10} {1:>10}".format(for_function_2[0],for_function_2[1])
        elif len_keys == 1:
            f_2 ="{0:>10}".format(for_function_2[0])

        print( f,tab, f_2, sep='\n')

    if b:
        b_values = b.values()
        b_func_values = [x for x in b_values]
        len_b = len(b_func_values)

        if len_b >= 4:
            tab = (('_') * 10  + ' ')*4
        else:
            tab= (('_') * 10 + ' ')*4


        if len_b >= 4:
            f_2 = "{0:>10} {1:>10} {2:>10} {3:>10}".format(b_func_values[0],b_func_values[1],b_func_values[2],b_func_values[3])
        elif len_b == 3:
            f_2 = "{0:>10} {1:>10} {2:>10}".format(b_func_values[0],b_func_values[1],b_func_values[2])
        elif len_b == 2:
            f_2 = "{0:>10} {1:>10}".format(b_func_values[0],b_func_values[1])
        elif len_b == 1:
            f_2 = "{0:>10}".format(b_func_values[0])

        print( tab , f_2 , sep='\n')



    if c:
        values_c = c.values()
        for_function_2_c = [x for x in values_c]
        len_keys_c = len(for_function_2_c)

        if len_keys_c > 4:
            tab = (('_')*10+' ') * 4
        else:
            tab = (('_')*10+' ') * len_keys_c


        if len_keys_c >= 4:
            f_2 ="{0:>10} {1:>10} {2:>10} {3:>10}".format(for_function_2_c[0],for_function_2_c[1],for_function_2_c[2],for_function_2_c[3])
        elif len_keys_c == 3:
            f_2 ="{0:>10} {1:>10} {2:>10}".format(for_function_2_c[0],for_function_2_c[1],for_function_2_c[2])
        elif len_keys_c == 2:
            f_2 ="{0:>10} {1:>10}".format(for_function_2_c[0],for_function_2_c[1])
        elif len_keys_c == 1:
            f_2 ="{0:>10}".format(for_function_2_c[0])

        print( tab, f_2, sep='\n')
    if d:
        d_values = d.values()
        d_func_values = [x for x in d_values]
        len_d = len(d_func_values)

        if len_d >= 4:
            tab = (('_') * 10  + ' ')*4
        else:
            tab= (('_') * 10 + ' ')*4


        if len_d >= 4:
            f_2 = "{0:>10} {1:>10} {2:>10} {3:>10}".format(d_func_values[0],d_func_values[1],d_func_values[2],d_func_values[3])
        elif len_d == 3:
            f_2 = "{0:>10} {1:>10} {2:>10}".format(d_func_values[0],d_func_values[1],d_func_values[2])
        elif len_d == 2:
            f_2 = "{0:>10} {1:>10}".format(d_func_values[0],d_func_values[1])
        elif len_d == 1:
            f_2 = "{0:>10}".format(d_func_values[0])

        print( tab , f_2 , sep='\n')



d_1 = {
    'Name':'AA',
    'Share':'100',
    'Price':'39.91',
    'Change':'7.71',
}

d_2 = {
    'Name':'IBM',
    'Share':'50',
    'Price':'106.11',
    'Change':'15.01',

}

d_3 = {
    'Name':'AA',
    'Share':'100',
    'Price':'39.91',
    'Change':'7.71',
}

d_4 = {
    'Name': 'IBM',
    'Share': '50',
    'Price': '106.11',
    'Change': '15.01',

}
Sheets(d_1,d_2,d_3,d_4)
