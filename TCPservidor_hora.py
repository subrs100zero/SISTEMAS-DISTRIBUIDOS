import socket
import threading
import time

def conexao_cliente(client, address):
    # Enviando o horário atual para o cliente
    horario_atual = time.ctime(time.time()) + '\n'
    client.sendall(horario_atual.encode())
    # Fechando o socket
    client.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('localhost', 20001)
print("Iniciando servidor na porta %s %s" % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    client, address = sock.accept()
    conexao = threading.Thread(target=conexao_cliente, args=(client, address,))
    conexao.start()
