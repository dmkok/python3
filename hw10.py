"""
hw10
Гипотеза Коллатца
может быть кратко выражена следующим образом:

берём любое натуральное число n, если оно чётное,
то делим его на 2 если нечётное, то умножаем на 3
и прибавляем 1 (получаем 3n + 1) над полученным
числом выполняем те же самые действия, и так далее.

Гипотеза Коллатца заключается в том, что какое бы
начальное число n мы ни взяли, рано или поздно мы
получим единицу.

Пример
Для числа 12:
12
6
3
10
5
16
8
4
2
1
Всего получаем 9 шагов.

Задача
Вычислить число шагов для числа n, согласно гипотезе
Коллатца необходимых для достижения этим числом единицы.
"""
print("введите натуральное число")
number = input()
number=int(number)
coutn =0
print(f"Для числа {number}")
while number != 1:
    if number % 2 == 0:
        number=number//2
        print(number)
        coutn+=1
    else:
        number=3*number+1
        coutn += 1
        print(number)
print(f"Всего получаем {coutn} шага(ов).")

# введите натуральное число
# 75
# Для числа 75
# 226
# 113
# 340
# 170
# 85
# 256
# 128
# 64
# 32
# 16
# 8
# 4
# 2
# 1
# Всего получаем 14 шага(ов).