import socket

# Step 1: Making Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Conect In Server
client_socket.connect(('localhost', 9999))

# Step 3: Massage In Server
client_socket.send("Hello Server!".encode())

# Step 4: Answer In Server
response = client_socket.recv(1024).decode()
print("Server says:", response)

# Step 5: Stop the Connection 
client_socket.close()
