"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time
start_time = time.time()
print("Problem 9 - the product abc is: ",[(a*b*c) for a in range(190,450) for b in range(190,450) for c in range(190,450) if a**2+b**2==c**2 and a+b+c==1000][0])
print("calculating time for problem 9: %s seconds" % (time.time() - start_time))

"""
Sum square difference 
Problem 6
The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

print("Problem 6 - the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum: ",(sum(i for i in range(101))**2)-(sum(i**2 for i in range(101))))


"""
Self powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
"""

print("Problem 48 - the last ten digits of the series: ",(str(sum(i**i for i in range(1001)))[-10:]))


"""
Champernowne's constant
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

new_list= "".join([str(i) for i in range(1,500000)])
print("Problem 40 - d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000= ", (int(new_list[0])*int(new_list[9])*int(new_list[99])*int(new_list[999])*int(new_list[9999])*int(new_list[99999])*int(new_list[999999])))