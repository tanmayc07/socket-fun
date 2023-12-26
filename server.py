import socket

serv_sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    proto=0
)

print(type(serv_sock))