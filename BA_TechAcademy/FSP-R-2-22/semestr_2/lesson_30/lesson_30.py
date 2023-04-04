# import os
# print(os.getcwd())

import csv
# with open('people.csv' , 'r') as file:
#     reader = csv.reader(file)
#     for x in reader:
#         print(x)


# with open('people.csv' , 'w' , newline='' , encoding='utf-8') as file:
#     write = csv.writer(file , delimiter=',')
#     write.writerow(['name','email','password','username','game'])
#     write.writerow(['rasul','test@gmail.com','password@','r','warfame'])
#     write.writerow(['rasulaka','test33@gmail.com','p@ssword@','rasulaka','warfame'])



with open('people.csv' , 'w' , newline='' , encoding='utf-8') as file:
    write = csv.writer(file , delimiter=',')
    write.writerow(['name','email','password','username','game'])
    write.writerow(['rasul','test@gmail.com','password@','r','warfame'])
    write.writerow(['rasulaka','test33@gmail.com','p@ssword@','rasulaka','warfame'])    