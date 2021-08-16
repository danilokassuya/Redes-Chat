import socket
import threading

print("------CLIENT------")


nickname = input("Escolha seu nome de usuario: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Forneça o IP da maquina: ")
IP_address = input()
print("Forneça a PORTA da maquina:")
Port = int(input())

client.connect((IP_address, Port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()