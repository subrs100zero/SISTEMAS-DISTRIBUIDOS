from datetime import datetime
from typing import List
from xmlrpc.server import SimpleXMLRPCServer

class MessageService:
    def __init__(self):
        self.message_list = []

    def store_message(self, message):
        self.message_list.append(message)
        print(f"Mensagem armazenada: {message}")

    def get_message_list(self):
        return self.message_list.copy()

    def get_server_ip(self):
        return "localhost"

    def get_server_date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(MessageService())
    print("Servidor pronto...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
