import socket

# Step 1: Making Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Address and Port bind
server_socket.bind(('localhost', 9999))

# Step 3: Start Listening
server_socket.listen(1)
print("Server is listening on port 9999...")

# Step 4: Client connection accept
conn, addr = server_socket.accept()
print(f"Connected with {addr}")

# Step 5: Data Recipt In Client
data = conn.recv(1024).decode()
print("Client says:", data)

# Step 6: Output In Client
conn.send("Hello Client, message received!".encode())

# Step 7: Connection বন্ধ করা
conn.close()

