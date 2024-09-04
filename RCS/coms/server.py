import socket

class Server:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.bind((self.host, self.port))
    self.server_socket.listen(1)
    print("Waiting for connection...")
    self.client_socket, address = self.socket.accept()
    print(f"Connection from {address}")
    self.robotInit()
    self.listenServer()

  def robotInit(self):
    pass

  def robotPeriodic(self):
    pass

  def robotEnd(self):
    pass

  def listenServer(self):
    try:
      while True:
        data = self.client_socket.recv(1024).decode("utf-8")
        if not data:
          break
        self.robotPeriodic()
    finally:
      self.client_socket.close()
      self.server_socket.close()
      self.robotEnd()
  
  def sendData(self, data):
    self.client_socket.sendall(data)