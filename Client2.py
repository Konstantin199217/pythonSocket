import socket
import threading

chat_socket = socket.socket()
address = ('127.0.0.1', 55555)
chat_socket.connect(address)

name = b"Homer"
chat_socket.send(name)

def send_message():
     while True:
        input_message = 'Homer: ' + input('> ')
        chat_socket.send(input_message.encode(encoding='ascii'))

def get_message():
    while True:
        getT_message = chat_socket.recv(1024)
        print(getT_message)

send_thread = threading.Thread(target=send_message)
send_thread.start()

get_thread = threading.Thread(target=get_message)
get_thread.start()