import socket

HOST = 'localhost'
PORT = 10000
ADDR = (HOST, PORT)
BUFSIZE = 4096
out_file = "image_3.png"

data = open(out_file, 'rb').read()

print(len(data))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(data)

client.close()
