import socket

Host_IP=socket.gethostbyname(socket.gethostname())
Host_Port=12345
ENCODER = 'utf-8'
ByteSize=1024

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((Host_IP, Host_Port))
server_socket.listen()

print(f"Server started at {Host_IP}:{Host_Port}")

client_socket, client_address = server_socket.accept()
client_socket.send((f"Connected to server at {Host_IP}:{Host_Port}").encode(ENCODER))

while True:
    Message = client_socket.recv(ByteSize).decode(ENCODER)
    if Message == "terminate":
        print("Client has terminated the connection.")
        break
    print(f"Message from client: {Message}")
    response = input("Enter your response: ")
    client_socket.send(response.encode(ENCODER))
    if response == "terminate":
        break

server_socket.close()