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
import subprocess
myfile=open("output.txt", "w") #для создания, если файла нет и очистки если уже был записан
myfile.close()
myfile=open("output.txt", "a")
myfile.write("/etc/passwd:\n")
cmd="cat /etc/passwd |cut -f 7 -d : |uniq -c |sort -u"
cat=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, universal_newlines=True)
output = cat.communicate()[0]
myfile.write(str(output))
myfile.write("\n/etc/group:\n")
cmd="cat /etc/group |cut -f 1,4 -d : "
cat=subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT, universal_newlines=True)
output = cat.communicate()[0]
myfile.write(str(output))
myfile.close()

