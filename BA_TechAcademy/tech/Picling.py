class Foo(object):
  def __init__(self, val=2):
     self.val = val
  def __getstate__(self):
     print("I'm being pickled")
     self.val *= 2
     return self.__dict__
  def __setstate__(self, d):
     print("I'm being unpickled with these values: " + repr(d))
     self.__dict__ = d
     self.val *= 3

import pickle
f = Foo()
f_data = pickle.dumps(f)
f_new = pickle.loads(f_data)



"""
Модуль pickle реализует бинарные протоколы для сериализации и десериализации структуры объекта Python. 
«Выделение» — это процесс, при котором иерархия объектов Python преобразуется в поток байтов, 
а «распаковывание» — обратная операция, при которой поток байтов (из двоичного файла или объекта, подобного байтам ) 
преобразуется обратно в иерархию объектов. Травление (и распаковка) также известно как «сериализация», 
«сортировка» 1 или «выравнивание»; однако, чтобы избежать путаницы, здесь используются термины «маринование» и «рассоливание».
"""
#https://stackoverflow.com/questions/1939058/simple-example-of-use-of-setstate-and-getstate