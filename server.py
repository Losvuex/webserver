import socket

s = socket.socket()
s.bind(('localhost', 8080)) # Привязываем серверный сокет к localhost и 8080 порту.
s.listen(1) # Начинаем прослушивать входящие соединения
conn, addr = s.accept() # Метод который принимает входящее соединение.

while True: # Создаем вечный цикл.
	data = conn.recv(1024) # Получаем данные из сокета.
	if not data:
		break
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8')) # Выводим информацию на печать.
conn.close()
