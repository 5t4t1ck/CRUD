"""
Crear un CRUD de algún negocio
"""

clients = "Diego,Juan,"

#1. Creamos la función create_client
def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("El cliente ya está en la lista de clientes")

#2. Creamos la funcion list_clients
def list_clients():
    global clients

    print(clients)

#Funcion de ayuda ','
def _add_comma():
    global clients

    clients += ','

#3 Creamos la función _print_walcome()
def _print_welcome():
    print("Bienvenido a mi pequeño negocio")
    print("*"* 50)
    print("¿Qué quieres hacer?")
    print("[C]rear cliente")
    print("[E]liminar cliente")

# 0 Ejecución del programa
if __name__ == '__main__':
    _print_welcome()
    command = input()
    if command == "C":
        client_name = input("Cual es el nombre del cliente: ")
        create_client(client_name)
        list_clients()
    elif command == "D":
        pass
    else:
        print("Comando invalido")

