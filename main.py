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

# 4 Creamos la función update_client()
def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", update_client_name + ",")
    else:
        print("El cliente no esta en la lista de clientes")

#5 Creamos la función delete_client()
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ",", "")
    else:
        print("El cliente no está en la lista de clientes")

#6 Creamos la función search_client()
def search_client(client_name):
    clients_list = clients.split(",")

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
        

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
    print("[L]eer clientes")
    print("[A]ctualizar cliente")
    print("[E]liminar cliente")
    print("[B]uscar cliente")

# 4 Refactoring de Cual es el nombre del cliente
def _get_client_name():
    return input("Cual es el nombre del cliente: ")


# 0 Ejecución del programa
if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command =="L":
        list_clients()
    elif command == "E":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "A":
        client_name = _get_client_name()
        update_client_name = input("Cual es el el nuevo nombre del cliente: ")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == "B":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("El cliente está en la lista de clientes")
        else:
            print("El cliente: {} no está en la lista de clientes".format(client_name))
    else:
        print("Comando invalido")

