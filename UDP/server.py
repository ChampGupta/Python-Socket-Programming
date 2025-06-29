import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

message, client_address=server_socket.recvfrom(1024)  # Receive a message from the client, up to 1024 bytes
print(f"Received message: {message.decode('utf-8')} from {client_address}")