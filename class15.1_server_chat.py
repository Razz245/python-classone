# 
#class15.1_server_chat.py
# Server Side Chat Application with Threading
# ==========================
# Class 15.1: Server Side Chat Application with Threading
import socket
import threading

# Running Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print("🟢 Server listening on port 9999...")

conn, addr = server_socket.accept()
print(f"Connected with {addr}")

# Info Cullecting Server
def receive_messages():
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("Client disconnected.")
            break
        print(f"\n💬 Client: {data}")

# Deferent Imfo
threading.Thread(target=receive_messages, daemon=True).start()

# Tranfer In Data
while True:
    msg = input("🧑‍💻 You: ")
    if msg.lower() == 'exit':
        conn.send("Server has left the chat.".encode())
        break
    conn.send(msg.encode())

conn.close()
server_socket.close()
