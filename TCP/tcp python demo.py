import socket
TCP_IP = ' '
TCP_PORT = 8000
BUFFER_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
conn.send(bytes('12,12','UTF-8'))
