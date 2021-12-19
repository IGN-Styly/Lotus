import socket
import socks

HEADER=64
PORT = 5050
IP = '127.0.1'
ADDR = (IP, PORT)
FORMAT= 'utf-8'
DISCONECT = '%!/DISCONECT/!%'

#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

def send(msg):
    msg = msg.encode(FORMAT)
    msg_lengh = len(msg)
    send_lengh = str(msg_lengh).encode(FORMAT)
    send_lengh +=b' ' * (HEADER - len(send_lengh))
    s.send(send_lengh)
    s.send(msg)
    print(s.recv(2048).decode(FORMAT))

send("Hello")
send(DISCONECT)
send("ayo")
