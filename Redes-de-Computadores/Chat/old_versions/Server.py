import socket
import select
import sys
import threading

listOfClients = []

def mainServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print("Forneça o IP da maquina: ")
    IP_adress = input()
    print("Forneça a PORTA da maquina:")
    PORT = int(input())
    try:
        server.bind((IP_adress, PORT))
    except:
        print("WARNING: Ip ou porta invalida - Server entrando em modo default ip:localhost:80")
        server.bind(("", 80))

    server.listen(100)
    
    while True:

        con, addr = server.accept()

        listOfClients.append(con)
        print(addr[0] + " conectado")
        threading.Thread(target=clientThread, args=(con, addr)).start()

# Função responsavel por controlar a thread de clientes do servidor
# Necessita da conexão e do ip do cliente
# Não há retorno

def clientThread(con, addr):
    con.send(b"Bem-vindo ao Chat!")

    while True:
        try:
            message = con.recv(2040)
            if message:
                # Printa a mensagem e o ip do usuario que enviou a mensagem no terminal do server.
                print(f"{addr[0]}: {message}")

                messagToSend = f"{addr[0]}: {message}"
                broadcast(messagToSend, con)
            else:
                remove(con)
        except:
            continue

# Função responsavel por enviar a mensagem para os clientes diferentes do usuario que mandou a mensagem
# Argumentos:
#    message: mensagem que será enviada
#    connection: conexão que a mensagem está sendo enviado
# Não há nenhum retorno

def broadcast(message, connection):
    for clients in listOfClients:
        if clients !=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

# Função responsavel por remover o objeto cliente da lista de clientes
# Argumentos: Objeto cliente
# Não há nenhum retorno
def remove(connection):
    if connection in listOfClients:
        listOfClients.remove(connection)

mainServer()