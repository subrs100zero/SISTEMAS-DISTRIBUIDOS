import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 20002)

# Enviando uma mensagem vazia para solicitar o horário
sock.sendto(''.encode(), server_address)

# Recebendo o horário do servidor
data, _ = sock.recvfrom(1024)
horario = data.decode()
print("Horário recebido do servidor:", horario)

# Fechando o socket
sock.close()
