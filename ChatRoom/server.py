import socket, threading

Host_IP=socket.gethostbyname(socket.gethostname())
Host_Port=12345
Encoder='utf-8'
ByteSize=1024

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((Host_IP,Host_Port))
server_socket.listen()

client_socket_list=[]
client_name_list=[]

def broadcast_message(message,messenger):
    for client in client_socket_list:
        try:
            if client == messenger:
                continue
            client.send(message)
        except Exception as e:
            print(f"Error sending message to a client: {e}")

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(ByteSize)
            broadcast_message(message, client_socket)
        except Exception as e:
            index=client_socket_list.index(client_socket)
            client_socket_list.remove(client_socket)
            client_socket.close()
            nickname=client_name_list[index]
            client_name_list.remove(nickname)
            broadcast_message(f"{nickname} has left the chat.", client_socket)
            break

def connect_client():
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected to {str(address)}")
        client_socket.send("Enter your nickname: ".encode(Encoder))
        nickname = client_socket.recv(ByteSize).decode(Encoder)
        client_name_list.append(nickname)
        client_socket_list.append(client_socket)
        print(f"Nickname of the client is {nickname}")
        broadcast_message(f"{nickname} has joined the chat.".encode(Encoder),client_socket)
        client_socket.send("You are now connected to the chat room.".encode(Encoder))
        
        thread = threading.Thread(target=receive_message, args=(client_socket,))
        thread.start()

print(f"Server is listening on {Host_IP}:{Host_Port}")
connect_client()