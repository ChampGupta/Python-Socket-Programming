import socket

# AF_INET is the address family for IPv4, SOCK_STREAM is the socket type for TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket. is module and after socket. is functions in socket module

print(socket.gethostname()) # Get the hostname of the machine
print(socket.gethostbyname(socket.gethostname())) # Get the IP address of the machine

# Bind the socket to a specific address and port
server_socket.bind((socket.gethostname(), 12345)) # Use the hostname and port
server_socket.listen() # Listen for incoming connections

while True:
    #Accept a connection from a client
    client_socket, client_address = server_socket.accept() # Accept the connection and get the client socket
    # print(type(client_socket)) # Print the type of the client socket
    print(client_socket) # Print the client socket object
    # print(type(client_address)) # Print the type of the client address
    print(client_address) # Print the client address
    print(f'Connection from {client_address} has been established!') # Print a message indicating that the connection has been established

    client_socket.send(bytes('Welcome to the server!', 'utf-8')) # Send a welcome message to the client in bytes format

    server_socket.close() # Close the client socket after sending the message
    break