import socket
import sys

sock = socket.socket()

def wait_messange():
    sock.bind(('', int(sys.argv[1]))) #Настройка сокета на конкретный порт
    sock.listen(2) # Максимальное количество соединений на сервере
    conn, addr = sock.accept() # Принимает данные пользователя (Отправителя)

    print('connected:', addr) # Печатает данные пользователя

    data = conn.recv(1024) # Устанавливает ограничения на сообщения по размерам
    print(data.decode('utf-8')) #
    conn.close() # Закрывает это говно

def send_messange():
    sock.connect(('localhost', int(sys.argv[2]))) #Соединение с сервером
    output = input()
    sock.sendall(output.encode('utf-8')) #Запрашивает сообщение у пользователя и отправляет его на сервер



if sys.argv[3] == 'True':
    wait_messange()
    send_messange()
else:
    send_messange()
    wait_messange()

sock.close() # Закрывает соединение
