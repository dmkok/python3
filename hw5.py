# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.
#
#
# Например:
#
# -> 2 1 8 4 2 3 5 7 10 18 82 2
# 6
print("введите неотрицательные числа, разделенные пробелом")
text = input()
text= text.split(" ")
#print(text)
for t in text:
    if t == '':
        text.remove(t)
text=sorted(text)
min=1
#print(text)
for i in text:
    if int(i)>min:
        break
    else:
        min=int(i)+1
print(min)