'''
таблица соответствия:
int -bool:
True == 1, True !=0 , True!=258 -- True
bool(1), bool(258) - True
True == 9 - False

False == 0, False != 1, False != 1000 --True
bool(0) - False

string-bool:
bool([2,8]), bool('True'), bool('False'), bool([{},{}]) -True длина (len) объекта !=0
bool(''), bool({}), bool([]) - False пустой объект

различия между input() и raw_input()
input() - всё преобразуется в str, есть в python 2 and 3
raw_input - нет в python 3. input() похож на raw_input()
в python 2 raw_input() возвращает str, input() берёт raw_input() и выполняет eval()
Основное: input() ожидает синтаксически правильного оператора python, а raw_input() -нет.

Изменения print между python2 и python3.
v2: print - оператор, v3 - функция
Изменение синтаксиса: v2: print "hello, world" v3: print("hello, world")
'''
