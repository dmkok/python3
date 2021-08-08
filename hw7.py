"""
Напишите программу, которая читает данные из файлов
/etc/passwd и /etc/group на вашей системе и выводит
следующую информацию в файл output.txt:
1. Количество пользователей, использующих все имеющиеся
интерпретаторы-оболочки.
( /bin/bash - 8 ; /bin/false - 11 ; ... )
2. Для всех групп в системе - UIDы пользователей
состоящих в этих группах.
( root:1, sudo:1001,1002,1003, ...)
"""
import os
myfile=open("output.txt", "w")
myfile.write("/etc/passwd:\n")
cmd="cat /etc/passwd |cut -f 7 -d : |uniq -c |sort -u"
myfile.write(str(os.popen(cmd).read()))
cmd="cat /etc/group |cut -f 1,4 -d : "
myfile.write("\n/etc/group:\n")
myfile.write(str(os.popen(cmd).read()))
myfile.close()

