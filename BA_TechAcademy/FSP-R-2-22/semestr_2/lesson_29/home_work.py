from googletrans import Translator
from os import path
try:
    with open('traslate.txt' , mode='w' , encoding='UTF-8') as trans:
        traslate=Translator()
        text = str(input('напиши текст для перевода = '))
        result = traslate.translate(text , src='en' , dest='ru')
        trans.write(result)
        trans.close()
except  Exception as err:
    print('Erorr',err)
# from_lang ='en' , to_lang = 'ru'




with open('home_work.txt', mode='w') as dred:
    def tablisa(*args):
        total=''
        for x in args:
            num=len(x)
            keygan=''
            valgan=''
            spisok=[]
            for key,value in x.items():
                keygan+=f'{key:>10} '
                for x in value:
                    valgan+=f'{x:>10} '
                valgan+='\n'
            keygan+='\n'
            valgan+='\n'
            tab=(("-")*10+' ')*num+'\n'
            total+=keygan+tab+valgan
        dred.write(total)


    home={
        'name': ['apple',2,3,4,'test'],
        'share': ['huawei',6,7,8,'test'],
        'price': ['samsung',10,11,12,'test'],
        'change': ['xiaomi',14,15,16,'test'],
        'proverka': ['honor',17,18,19,'test'],
    }
    tablisa(home,home)



patg_thefile = "D:\RASUL"
path_t_f=path.isfile(patg_thefile)
print(path_t_f)