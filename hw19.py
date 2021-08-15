"""
Написать dns сервер.
Сервер должен принимать соединения по протоколу udp.
Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
* Доп задание: иметь возможность переопределять записи клиентами:
* ADD my.google.com:228.228.228.228
"""
#!/usr/bin/python
#UDP echo Server
import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1",5001))
records={'ya.ru':'77.88.55.66', 'google.com':'173.194.73.102','cisco.com':'72.163.4.185', 'aws.amazon.com':'13.224.187.73'}
print ("UDP -Echo Server listening on port 5001:")
while True:
    data,address=server_socket.recvfrom(512)
    print (f"{address}, :ask , {data}")
    data=str(data.decode())
    answer=True
    ip_a=""
    for key,value in records.items():
        if data==key:
            ip_a=value
    if data[:4]=="ADD ":
        delitomer=data.find(":")
        domain=data[4:delitomer]
        ip=data[delitomer+1:]
        records[domain]=ip
        print(f"{domain}:{ip}")
        ip_a="Запись добавлена"
    if ip_a =="":
        ip_a="Нет такой записи"
    server_socket.sendto(ip_a.encode(),address)



"""
client
"""

#!/usr/bin/python
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	data=input('Type Something(q or Q to exit:)')
	if data=='q' or data=='Q':
		client_socket.close()
		break
	else:
		client_socket.sendto(data.encode(),('127.0.0.1', 5001))
		newdata=client_socket.recvfrom(512)
		newdata=newdata[0].decode()
		print (f"ip address for {data} : {newdata}")
