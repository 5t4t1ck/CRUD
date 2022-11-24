"""
Crear un CRUD de algún negocio
"""
import sys

clients = [
    {
        "name":"Diego",
        "company":"UIDE",
        "email": "disaavedraga@uide.edu.ec",
        "position":"Docente",
    },
    {
        "name":"Juan",
        "company":"CNT",
        "email":"juan@cnt.gob.ec",
        "position":"Técnico",
    }
]

#1. Creamos la función create_client
def create_client(client):
    global clients
    
    if client_name not in clients:
        clients.append(client)
    else:
        print("El cliente ya está en la lista de clientes")

#2. Creamos la funcion list_clients
def list_clients():
    for idx, client in enumerate(clients):
        print("{uid} |{name}|{company}|{email}|{position}".format(
            uid=idx,
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"],
        ))

# 4 Creamos la función update_client()
def update_client(client_id, update_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('El cliente {} no esta en la lista de clientes'.format(client_name))

#5 Creamos la función delete_client()
def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[client_id]
            break

#6 Creamos la función search_client()
def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True
        

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

#Implementamo _get_client_field()
def _get_client_field(field_name):
    field = None

    while not field:
        field = input("Cuál es el nombre del cliente {}:".format(field_name))

    return field

#Implementando _get_client_from_user()
def _get_client_from_user():
    client = {
        "name": _get_client_field("name"),
        "company": _get_client_field("company"),
        "email": _get_client_field("email"),
        "position": _get_client_field("position"),
    }
    return client


# 4 Refactoring de Cual es el nombre del cliente
def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input("Cual es el nombre del cliente: ")

        if client_name == "exit":
            client_name = None
            break
        
    if not client_name:
        sys.exit()

    return  client_name


# 0 Ejecución del programa
if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == "C":
        client_name = {
            "name": _get_client_field("name"),
            "company":_get_client_field("company"),
            "email":_get_client_field("email"),
            "position":_get_client_field("position"),
        }
        create_client(client_name)
        list_clients()
    elif command =="L":
        list_clients()
    elif command == "E":
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == "A":
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command == "B":
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('El cliente: {} esta en la lista de clientes'.format(client_name))
        else:
            print('El cliente: {} no esta en la lista de clientes'.format(client_name))
    else:
        print('Comando Invalido')