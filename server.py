import socket

serv_sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)

print(type(serv_sock))
print(serv_sock.fileno())

serv_sock.bind(('127.0.0.1', 6543))

backlog = 10
serv_sock.listen(backlog)

while True:
    client_sock, client_addr = serv_sock.accept()
    print(f"Accepted connection from {client_addr}")

    chunks = []
    while True:
        data = client_sock.recv(2048)
        if not data:
            break
        chunks.append(data)

    client_sock.sendall(b''.join(chunks))
    client_sock.close()
