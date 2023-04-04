# try:
#     file = open("test.txt")

#     # print(file.read(10))
#     # print(file.read(10))
#     # print(file.read(10))
#     # content = file.read()
#     # print(content)

#     # file.seek(10)
#     # print(file.read(1999))

#     # for roq in file:
#     #     print(roq)

#     # print(file.readline())
#     # print(file.readline())
#     # file.seek()
#     # print(file.readlines())
# except Exception as err:
#     print(err)
# finally:
#     file.close()


# with open('test.txt') as file:
#     for row in file:
#         print(row)

# with open('test_write.txt', mode = 'w') as file: # 'w' -> создает если нет, и пишет внутри файла, каждый раз когда записывает то удаляет старый текст
#     file.write("Something that you dont know")
#     file.writelines("")


# with open('test_write.txt', mode = 'a') as file:
    # file.write("\n Another random text")

# with open('test_write.txt', mode = 'ab') as file:
#     file.write(b"\n Another random text")

# with open('test_write.txt', mode = 'rb') as file:
#     for row in file:
#         print(row)



#    *   
#   ***
#  ***** 
#    *

with open('text_smm.txt', mode='w') as dred:
    def mirror(text):
        text=text[0::]
        text=text.split()
        tex=len(text)
        text.reverse()
        tett=max(text, key=len)
        tett=len(tett)
        tetto=tett+4
        f='*'
        total=''
        i=1
        for x in text:
            xen=' *\n* '
            probel=' '
            now=tett-len(x)
            new=now*probel
            if len(text)>i:
                total+=x+(new+xen)
                i+=1
            elif len(text)<=i:
                total+=x+new
        ff=f'{f*tetto}\n* {total} *\n{f*tetto}'
        dred.write(ff)
    print(mirror('Abdurahmon Shahriyorov Javlon ogli'))

