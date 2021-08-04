'''https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2. (Please note that the palindromic number,
in either base, may not include leading zeros.)

Напишите программу, которая решает описанную выше задачу и печатает ответ.'''
max_number = 1000001
sum=0
for i in range(1, max_number+1):
    rev10 = str(i)[::-1] #переворачиваем 10
    if rev10==str(i): #сравниваем строки 10
        binary=str(bin(int(rev10)))[2:] #конвертируем
        rev_bin=binary[::-1] #переворачиваем 2
        if binary==rev_bin: #сравниваем строки 2
            sum=sum+i
print("sum= ",sum)


