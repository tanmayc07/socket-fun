import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect(('127.0.0.1', 6543))

client_sock.sendall(b'Sending some data!')
client_sock.shutdown(socket.SHUT_WR)

chunks = []
while True:
    data = client_sock.recv(2048)
    if not data:
        break
    chunks.append(data)

print(f"Received {b''.join(chunks)}")

client_sock.close()