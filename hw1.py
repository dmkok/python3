'''
int  | 4849             | 0
str  | '"hello world"   | "1"
bool | True==1(int)     | False==0(int)


различия между input() и raw_input()
input() - всё преобразуется в str, есть в python 2 and 3
raw_input - нет в python 3. input() похож на raw_input()
в python 2 raw_input() возвращает str, input() берёт raw_input() и выполняет eval()
Основное: input() ожидает синтаксически правильного оператора python, а raw_input() -нет.

Изменения print между python2 и python3.
v2: print - оператор, v3 - функция
Изменение синтаксиса: v2: print "hello, world" v3: print("hello, world")
'''
