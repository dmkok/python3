"""
Написать функцию-генератор, которая объединяет два отсортированных итератора.
Результирующий итератор должен содержать последовательность в
которой содержатся все элементы из каждой коллекции, в упорядоченном виде.

list(merge((x for x in range(1,4)),(x for x in range(2,5)))) == [1,2,2,3,3,4]
hw21: Решение вида yield from sorted(list(iter1)+list(iter2)) - не принимается.
"""
def merge(it1, it2):
    element1 = next(iter(it1), None)
    element2 = next(iter(it2), None)
    try:
        while element1 is not None or element2 is not None:#цикл пока итераторы не закончились
             if element1 is None or (element2 is not None and element1>element2):#сравнение элементов или возвращение element2, если итератор1 закончился
                yield element2
                element2 = next(iter(it2), None)
             else:
                yield element1
                element1 = next(iter(it1), None)
    except StopIteration:
        return ("error")
numb1=(x for x in range(1,8))
numb2=(x for x in range(2,5))
print(list(merge(numb1,numb2)))
