


a=[10,20,30,40,50,60,40,45]
x=[101,50,55,100,51,60]
zip_a = []
for i in range(len(a)):
    for j in range(len(x)):
        # if x[j] >= 45:
        #     x.pop()
            
        zip_a.append([a[i] , x[j]])
print(zip_a)
        
"""
Что такое заморозка пипсов в Python?
pip freeze устанавливает только те пакеты, которые были установлены с помощью команды pip install . 
Однако pip — не единственный менеджер пакетов Python. 
Мы также можем использовать Chocolatey, Conda, SetupTools и т. д., 
и они не поддерживаются заморозкой пипсов, поэтому нам придется прописывать их вручную в требованиях. 
текстовый файл
"""


