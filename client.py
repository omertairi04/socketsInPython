import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at IP 127.0.0.1 and port 5555
s.connect(('127.0.0.1', 5555))

# Receive data from the server
message = s.recv(1024)  # bytes

# Close the connection
s.close()

# Decode and print the message
print(message.decode())


