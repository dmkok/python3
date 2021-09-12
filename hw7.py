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
myfile.write("\n/etc/group:\n")
myfile.close()
#создание словаря вида user:UID
cmd="cat /etc/passwd |cut -f 1 -d :"
cmd2="cat /etc/passwd |cut -f 3 -d :"
u=str(os.popen(cmd).read())
u_list=list(u.split("\n"))
for t in u_list:
    if t == '':
        u_list.remove(t)
uid=str(os.popen(cmd2).read())
uid_list=list(uid.split("\n"))
for t in uid_list:
    if t == '':
        uid_list.remove(t)
u_uid=dict(zip(u_list,uid_list))#словарь user:UID
#создание словаря вида group:UID
cmd="cat /etc/group |cut -f 1 -d : "
cmd2="cat /etc/group |cut -f 4 -d : "
groups=str(os.popen(cmd).read())
groups=list(groups.split("\n"))
users=str(os.popen(cmd2).read())
users=list(users.split("\n"))
for i in range(len(users)):
    if users[i] != '':
        for key, value in u_uid.items():#если в группе один пользователь
            if users[i] == key:
                users[i] = value #замена user на uid
        for j in users[i]:#если в группе несколько пользователей
            if j==',':
                u2=list(users[i].split(","))
                for n in range(len(u2)):
                    for key, value in u_uid.items():
                        if u2[n] == key:
                            u2[n] = value #замена user на uid
                users[i]=",".join(u2)
groups_users=dict(zip(groups,users))#словарь вида group:UID
#создание словаря вида user:GID
cmd="cat /etc/passwd |cut -f 1 -d :"
cmd2="cat /etc/passwd |cut -f 4 -d :"
u=str(os.popen(cmd).read())
u_list=list(u.split("\n"))
for t in u_list:
    if t == '':
        u_list.remove(t)
gid=str(os.popen(cmd2).read())
gid_list=list(gid.split("\n"))
for t in gid_list:
    if t == '':
        gid_list.remove(t)
u_gid=dict(zip(u_list,gid_list))#словарь user:GID
for group, uid2 in groups_users.items():
    tmp=''
    tmp=uid2
    for user, gid2 in u_gid.items():
        if group == user:
            groups_users[group]=str(gid2)+","+str(tmp)


del_k=False
for key, value in groups_users.items():#поиск и удаление пустого элемента в словаре
    if key=='' and value=='':
        del_key=''
        del_k=True
if del_k==True:
    del groups_users[del_key]
for key, value in groups_users.items():
    out_str=(f"{key}: {value}")

myfile=open("output.txt", "a")
for key, value in groups_users.items():
    out_str=(f"{key}: {value}\n")
    myfile.write(out_str)
myfile.close()

