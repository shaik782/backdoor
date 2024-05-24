import socket
import threading

HOST_IP = "127.0.0.1"
HOST_PORT = 32001

def handle_client(client_socket, client_address):
    print(f"Client connecté depuis : {client_address}")

    while True:
        # Recevoir un message du client
        message_received = client_socket.recv(1024).decode()
        if not message_received:
            break
        print(f"Client: {message_received}")

        # Envoyer un message au client
        message_sent = input("Moi: ")
        client_socket.sendall(message_sent.encode())

    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT} . . .")

while True:
    # Attendre une nouvelle connexion
    client_socket, client_address = server_socket.accept()

    # Démarrer un nouveau thread pour gérer le client
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
