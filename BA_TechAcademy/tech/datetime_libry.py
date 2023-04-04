

from datetime import time
from datetime import date
from datetime import timedelta
from datetime import datetime

# - %d: день месяца в виде числа
# - %m: порядковый номер месяца
# - %y: год в виде 2-х чисел
# - %Y: год в виде 4-х чисел
# - %H: час в 24-х часовом формате
# - %M: минута
# - %S: секунда



dt = datetime.strptime("30/08/2018", "%d/%m/%Y")
print(dt)
 
dt = datetime.strptime("29/03/2018 10:40", "%d/%m/%Y %H:%M")
print(dt)     
 
dt = datetime.strptime("06-28-2018 09:20", "%m-%d-%Y %H:%M")
print(dt)     

dt = datetime.strptime('2018-06-28', '%Y-%m-%d')
print(dt)

import locale
print(locale.setlocale(locale.LC_ALL,""))
# now = datetime.now()
# print(now.strftime('%Y-%m-%d (%a)'))
# print(now.strftime('%Y %B %d число (%A)'))

from datetime import timedelta

d1 = timedelta(days=5 , hours=4 , minutes=50)
d2 = timedelta(days=3,hours=4,minutes=50)
print(d1-d2)

my_birth_day = date(2003 , 11 ,30)
delta = date.today() - my_birth_day
print(type(delta))
my_age = int(delta.days/365)
print(my_age)


jovo_bithday = date(2002 , 4 , 1)

i_older = my_birth_day < jovo_bithday
print(i_older)

#https://all-python.ru/osnovy/modul-datetime.html#datetime
def now():
    return None