import socket
from NN.my_cnn import handwritingDetection
import binascii


def hexint(b):
    return int(binascii.hexlify(b), 16)

HOST = '0.0.0.0'
PORT = 80
ADDR = (HOST, PORT)
BUFSIZE = 1448 #strange stuff but, it is maximum buffer size....

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

detector = handwritingDetection("/home/yenq/MIET/ML/Lab4/server/NN/model/model.ckpt")

print('Listening ...')

while True:
    conn, addr = serv.accept()
    print('\nclient connected ... ', addr)
    myfile = open('out.png', 'wb')

    length = hexint(conn.recv(4))
    down = 0

    while down < length:
        data = conn.recv(BUFSIZE)
        down+=len(data)
        myfile.write(data)

    myfile.close()
    res = detector.detect('out.png')
    conn.send(res)
    print(res)
    conn.close()
    print('client disconnected')
