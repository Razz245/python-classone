# Client Side Chat Application with Threading
# Importing Libraries
# ==========================
# Class 15.2: Client Side Chat Application with Threading
# ==========================
#class15.2_client_chat.py
import socket
import threading

# Making Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))
print("🟢 Connected to the Server!")

# Function to receive messages from server
def receive_messages():
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            print("❌ Server disconnected.")
            break
        print(f"\n💬 Server: {data}")

# Received in Deferent Thred
threading.Thread(target=receive_messages, daemon=True).start()

# Tranfer in Info
while True:
    msg = input("🧑‍💻 You: ")
    if msg.lower() == 'exit':
        client_socket.send("Client has left the chat.".encode())
        break
    client_socket.send(msg.encode())

client_socket.close()
