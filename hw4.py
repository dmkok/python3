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
print("введите неотрицательные цисла, разделенные не цифровым литералом")
text = input()
text2=text
text=re.split('\D', text)
sum=0
for i in text:
    if (len(i)!=0):
        i=int(i)
        sum+=i
print(sum)


l = len(text2)
sum2=0
i = 0
while i < l:
    s_int = ''
    a = text2[i]
    while '0' <= a <= '9':
        s_int+= a
        i+= 1
        if i < l:
            a = text2[i]
        else:
            break
    i+= 1
    if s_int != '':
        sum2+=int(s_int)

print(sum2)
