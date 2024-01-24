# client.py
from xmlrpc.client import ServerProxy

# Cliente para servidor local
local_server = ServerProxy('http://localhost:8000/')

# Cliente para servidor remoto (substitua 'remote_server_url' pelo URL do servidor remoto)
remote_server_url = 'http://endereco-do-servidor-remoto:porta/'
remote_server = ServerProxy(remote_server_url)

try:
    # Acessar função para obter data e hora do servidor local
    local_datetime = local_server.get_datetime()
    print(f"Data e hora do servidor local: {local_datetime}")

    # Acessar função para obter a quantidade de chamadas recebidas no servidor local
    local_call_count = local_server.get_call_count()
    print(f"Quantidade de chamadas recebidas no servidor local: {local_call_count}")

    # Acessar função para obter data e hora do servidor remoto
    remote_datetime = remote_server.get_datetime()
    print(f"Data e hora do servidor remoto: {remote_datetime}")

    # Acessar função para obter a quantidade de chamadas recebidas no servidor remoto
    remote_call_count = remote_server.get_call_count()
    print(f"Quantidade de chamadas recebidas no servidor remoto: {remote_call_count}")

except Exception as e:
    print(f"Erro ao chamar a função remota: {e}")
