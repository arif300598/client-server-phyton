import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 65435
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    PESAN = input("pesan terkirim :")
    s.send(PESAN.encode())
    
    data = s.recv(BUFFER_SIZE)
    print(PESAN)
    
conn.close()
print(data)