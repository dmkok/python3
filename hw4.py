# строенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.
#
# Например:
#
# -> 12 12 12
# 36
#
# -> 123dfgdr%0&45ty-45--900
# -777
import re
print("введите неотрицательные числа, разделенные не цифровым литералом")
text = input()
text=re.findall('[-]?\d+',text)
print(text)
sum=0
for i in text:
    if (len(i)!=0):
        i=int(i)
        if i <0:
            i=abs(i)
        sum+=i
print(sum)
