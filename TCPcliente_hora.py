import socket

def receber_horario(sock):
    data = sock.recv(2048)
    horario = data.decode()
    print("Horário recebido do servidor:", horario)
    sock.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 20001)
print("Conectando %s porta %s" % server_address)
sock.connect(server_address)

# Iniciando a thread para receber o horário do servidor
recepcao = threading.Thread(target=receber_horario, args=(sock,))
recepcao.start()

# Aguardando a thread de recepção terminar antes de encerrar o cliente
recepcao.join()
