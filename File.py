import socket
import sys
from threading import Thread

def wait_messange():
    sock = socket.socket()
    sock.bind(('', int(sys.argv[1]))) #Настройка сокета на конкретный порт
    sock.listen(2) # Максимальное количество соединений на сервере
    conn, addr = sock.accept() # Принимает данные пользователя (Отправителя)

    print('connected:', addr) # Печатает данные пользователя

    data = conn.recv(1024) # Устанавливает ограничения на сообщения по размерам
    print(data.decode('utf-8')) #
    conn.close() # Закрывает это говно
    sock.close()

def send_messange():
    sock2 = socket.socket()
    sock2.connect(('localhost', int(sys.argv[2]))) #Соединение с сервером
    output = input()
    sock2.sendall(output.encode('utf-8')) #Запрашивает сообщение у пользователя и отправляет его на сервер
    sock2.close()

variable = Thread(target=wait_messange, args=())
variable2 = Thread(target=send_messange, args=())

variable.start()
variable2.start()
variable.join()
variable2.join()