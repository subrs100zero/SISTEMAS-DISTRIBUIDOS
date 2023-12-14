import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 20002)
print("Iniciando servidor na porta %s %s" % server_address)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)
    horario_atual = time.ctime(time.time()) + '\n'
    sock.sendto(horario_atual.encode(), address)
