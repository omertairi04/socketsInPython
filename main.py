import socket

# socket with tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip addr and port
s.bind(('127.0.0.1', 5555))

s.listen()

while True:
    client, address = s.accept()
    print(f"Connected to {address} ")
    client.send(f"You are connected!".encode())
    client.close()


 
