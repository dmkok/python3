"""
Надо написать функцию которая возвращает N-мерный массив
с ширинами заданными в аргументе списком из N элементов:
n_arr([2,2])
>> [[“”,“”],[“”,“”]]
n_arr([2,2,2])
>> [[[“”,“”],[“”,“”]], [[“”,“”],[“”,“”]]]
решение без изобретения велосипеда
"""
import numpy as np
def n_arr(*args):
    arr0 = np.empty(args)
    arr = arr0.astype('str')
    for i in np.nditer(arr, op_flags=['readwrite']):
        i[...]=''
    return arr
res=n_arr(2,2,2)




"""
или
from numpy import empty
n_arr=empty([2,2,2,2])
"""

