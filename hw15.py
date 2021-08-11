"""
Написать класс router.
Должен иметь методы добавить/удалить/вывести список ip address.
Должен иметь методы добавить/удалить/вывести список ip routes.
Есть маршруты к непосредственно-подключенным сетям:
если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
значит у него должен быть маршрут:
к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.
Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
то надо проверять доступен ли gateway.
Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.
Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
до которого у нас пока еще нет маршрута, то должен вылетать exception.
Например:
Добавляем ip-address 192.168.5.14/24 eth1.
Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.
Итого - 1 интерфейс и 3 маршрута в таблице.
hw15: docstrings, комментарии, демонстрации и прочий код необходим для проверки качетсва класса.
"""
import ipaddress
class Router():
    "class router"
    def __init__(self, name): # создаем роутер с именем
        self.name =name
        self.list_ip = list() # список для ip адресов
        self.list_routes = dict()  #словарь для маршрутов (gateway:network)
        print(f"роутер {name} создан")
    def add_ip(self,ip_addr):
        "метод добавления ip адреса"
        self.list_ip.append(ipaddress.ip_interface(ip_addr))
        print(f"ip адрес {ip_addr} добавлен для интерфейса")
    def del_ip(self, ip_addr):
        del_list = list() #список для зависимых от ip адреса маршрутов
        del_list.clear()
        for key,value in self.list_routes.items(): #ищем зависимый маршрут
            if ipaddress.ip_address(ipaddress.ip_address(key)) in ipaddress.ip_network(ipaddress.ip_interface(ip_addr).network):
                del_list.append(ipaddress.ip_address(key))
        for l in del_list:
            self.list_routes.pop(str(l))#удаляем связанный маршрут
        self.list_ip.remove(ipaddress.ip_interface(ip_addr))
        print(f"Интерфейс {ipaddress.ip_interface(ip_addr)} удален")
    def sh_ip(self):
        "метод вывода списка ip адресов"
        print("Список локальных ip адресов маршрутизатора:", )
        for i in self.list_ip: print(i)
    def add_r(self, net, gateway):
        "метод добавления маршрута"
        exception=False
        add=False
        find=True
        for i in self.list_ip: # просматриваем список локальных сетей для, если gateway входит в них, то добавляем маршрут
            if find==True: # нужно ли искать дальше
                if ipaddress.ip_address(gateway) in ipaddress.ip_network(i.network):
                    self.list_routes[f"{ipaddress.ip_address(gateway)}"]=f"{ipaddress.ip_network(net, strict=False)}"
                    print(f"ОК, маршрут до {net} добавлен")
                    find=False
                else:
                    exception=True
        if exception==True: #если gateway не было в списке локальных сетей, то проверяем его в уже имеющихся маршрутах
            for key, value in self.list_routes.items():
                if ipaddress.ip_address(gateway) in ipaddress.ip_network(value):
                    add=True # для избежания ошибки dictionary changed size during iteration
                    print(f"ОК, маршрут до {net} добавлен")
                    exception=False
                    find = False
                else:
                    exception=True
            if add==True:
                self.list_routes[f"{ipaddress.ip_address(gateway)}"] = f"{ipaddress.ip_network(net, strict=False)}"
        if exception==True and find==True:
            print(f"Exception, невозможно добавить маршрут к сети {net} через {gateway}")
    def del_r(self,route):
        del_list = dict()  # список для зависимых маршрутов от удаляемого маршрутов
        del_list.clear()
        for key, value in self.list_routes.items(): #ищем зависимый маршрут
            if ipaddress.ip_network(route)==ipaddress.ip_network(value):
                del_list[f"{ipaddress.ip_address(key)}"]=f"{ipaddress.ip_network(value)}"
        for l in del_list:
            self.list_routes.pop(str(l)) #удаляем связанный маршрут
        for key,value in self.list_routes.items():
            if value==route:
                self.list_routes.pop(route) #удаляем  маршрут
        print(f"Маршрут {route} удален")
    def sh_routes(self):
        "метед вывода списка маршрутов"
        print("Список доступных маршрутов:")
        for i in self.list_ip: print(i.network) #для подключенных через интерфейсы
        for key, value in self.list_routes.items(): print(value, 'via', key) # для доступных через gateway в сети

print("Из примера:")
router=Router('R')
router.add_ip('192.168.5.14/24')
router.add_r('172.16.0.0/16','192.168.5.1')
router.add_r('172.24.0.0/16','192.168.8.1')
router.add_r('172.24.0.0/16','172.16.8.1')
router.sh_ip()
router.sh_routes()


print("\nДополнительные проверки \n")
router1 = Router('R1')
router1.add_ip('192.168.1.2/24')
router1.add_ip('192.168.2.2/24')
router1.sh_ip()
router1.add_r('172.16.1.0/24','192.168.1.100')
router1.add_r('172.16.100.0/24','192.168.100.100')
router1.add_r('172.16.2.0/24','192.168.2.10')
router1.add_r('172.16.3.0/24','172.16.1.10')
router1.sh_routes()
router1.del_r('172.16.1.0/24')
router1.del_ip('192.168.2.2/24')
router1.sh_ip()
router1.sh_routes()