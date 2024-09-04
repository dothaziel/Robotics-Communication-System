import socket

def handle_keys(data):
  print(data)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)
print("Waiting for connection...")
client_socket, address = server_socket.accept()
print(f"Connection from {address}")

try:
  while True:
    data = client_socket.recv(1024).decode("utf-8")
    if not data:
      break
    handle_keys(data)
    

finally:
  client_socket.close()
  server_socket.close()