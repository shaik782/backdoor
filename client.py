import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST_IP, HOST_PORT))

while True:
    # Envoyer un message au serveur
    message_sent = input("Moi: ")
    client_socket.sendall(message_sent.encode())

    # Recevoir un message du serveur
    message_received = client_socket.recv(1024).decode()
    print(f"Serveur: {message_received}")

client_socket.close()

