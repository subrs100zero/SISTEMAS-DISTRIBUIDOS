# server.py
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime

# Classe que define as funções do servidor
class RPCFunctions:
    def __init__(self):
        self.call_count = 0

    def get_datetime(self):
        return datetime.datetime.now().isoformat()

    def get_call_count(self):
        self.call_count += 1
        return self.call_count

# Configuração do servidor
server = SimpleXMLRPCServer(('localhost', 8000), logRequests=True)

# Registrar as funções no servidor
server.register_instance(RPCFunctions())

# Rodar o servidor
print("Servidor RPC em execução. Pressione Ctrl+C para encerrar.")
server.serve_forever()
