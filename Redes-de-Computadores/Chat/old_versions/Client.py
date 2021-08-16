import socket
import select
import sys
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

print("Forneça o IP da maquina: ")
IP_address = input()
print("Forneça a PORTA da maquina:")
Port = int(input())
servidor.connect((IP_address, Port)) 

while True: 
  
    sockets_list = [sys.stdin, servidor] 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == servidor: 
            message = socks.recv(2048) 
            print (message) 
        else: 
            message = sys.stdin.readline() 
            servidor.send(message) 
            sys.stdout.write("<Você>") 
            sys.stdout.write(message) 
            sys.stdout.flush() 
servidor.close() 