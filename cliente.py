from xmlrpc.client import ServerProxy

def run_client():
    server = ServerProxy("http://localhost:8000/")
    
    # Exemplo de utilização das funções remotas
    server.store_message("Olá, mundo!")
    server.store_message("Como você está?")
    
    print("Mensagens no servidor:", server.get_message_list())
    print("IP do servidor:", server.get_server_ip())
    print("Data e hora do servidor:", server.get_server_date_time())

if __name__ == "__main__":
    run_client()
