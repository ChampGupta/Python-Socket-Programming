import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
client_socket.connect((socket.gethostname(), 12345)) # Connect to the server using the hostname and port 

message=client_socket.recv(1024) # Receive a message from the server, up to 1024 bytes
print(message.decode('utf-8')) # Decode the message from bytes to string and print it
client_socket.close() # Close the client socket after receiving the message