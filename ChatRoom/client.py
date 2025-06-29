import socket, threading

Dest_IP = socket.gethostbyname(socket.gethostname())
Dest_Port = 12345
Encoder = 'utf-8'
ByteSize = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((Dest_IP, Dest_Port))

nickname = input("Choose a nickname: ")
def receive_message():
    while True:
        try:
            message = client_socket.recv(ByteSize).decode(Encoder)
            if message == "Enter your nickname: ":
                client_socket.send(nickname.encode(Encoder))
            else:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            break

def send_message():
    while True:
        try:
            message = f"{nickname}: {input("")}"
            client_socket.send(message.encode(Encoder))
        except Exception as e:
            print(f"Error sending message: {e}")
            client_socket.close()
            break

recieve_thread = threading.Thread(target=receive_message)
recieve_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()