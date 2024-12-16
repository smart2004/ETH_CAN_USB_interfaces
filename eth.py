# socket для Ethernet:
import socket

# Создание сокета
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
s.connect(('localhost', 8080))

# Отправка данных
s.sendall(b'Hello, Ethernet!')

# Получение ответа
data = s.recv(1024)
print('Received', repr(data))

# Закрытие соединения
s.close()

# socket: Это встроенная библиотека Python для работы с сокетами, которая позволяет реализовать сетевые протоколы и обмен данными по Ethernet.

# import socket
# asyncio: Для асинхронного программирования и работы с сетевыми соединениями. Подходит для создания высокопроизводительных сетевых приложений.

# import asyncio
# Twisted: Это асинхронный фреймворк для сетевых приложений, который поддерживает множество протоколов и может быть использован для создания серверов и клиентов.

# pip install twisted
