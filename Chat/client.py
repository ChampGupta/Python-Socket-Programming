import socket

Dest_IP = socket.gethostbyname(socket.gethostname())
Dest_Port = 12345
ENCODER = 'utf-8'
ByteSize = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((Dest_IP, Dest_Port))

while True:
    Message=client_socket.recv(ByteSize).decode(ENCODER)
    if Message == "terminate":
        print("Server has terminated the connection.")
        break
    print(f"Message from server: {Message}\n")
    response = input("Enter your response: ")
    client_socket.send(response.encode(ENCODER))
    if response == "terminate":
        break

client_socket.close()